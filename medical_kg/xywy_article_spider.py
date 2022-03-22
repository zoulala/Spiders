#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xywy_article_spider.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-07-12
# brief:    
#
# cmd>e.g:  
# *****************************************************

# resource http://www.xywy.com/n_map/p_2

import re
import json
import os
import datetime
from lxml import etree
from .xywy_spider import XywySpider

class ArticleSpider(XywySpider):
    '''文章爬取类：健康类/疾病类'''

    def __init__(self):
        super(ArticleSpider,self).__init__()
        self.articles = set()
        self.articlepkl = 'article.json'

        self.dis_articles = set()  # 疾病关联的文章
        self.disarticlepkl = 'dis_article.json'

        self.dis_done_articles = set()  # 已经处理的疾病关联文章及推荐文章
        self.disdonearticlepkl = 'dis_done_article.json'
        self._load_dis_done_article()

    def __del__(self):
        pass
        # self._save_article(list(self.dis_done_articles),self.disdonearticlepkl)


    def _save_article(self, objs,filename):
        with open(filename,'w') as sf:
            json.dump(objs, sf, indent=4)

    def _load_article(self):
        if os.path.exists(self.articlepkl):
            with open(self.articlepkl,'r') as f:
                self.articles = set(json.load(f))

    def _load_dis_done_article(self):
        if os.path.exists(self.disdonearticlepkl):
            with open(self.disdonearticlepkl,'r') as f:
                self.dis_done_articles = set(json.load(f))

    def _load_dis_articles(self,path='disease_data'):

        if os.path.exists(self.disarticlepkl):
            with open(self.disarticlepkl,'r') as f:
                self.dis_articles = set(json.load(f))
                print(len(self.dis_articles))
            return

        files = os.listdir(path)
        for file in files:
            if not file.endswith('json'):continue
            filename = os.path.join(path,file)
            with open(filename,'r') as f:
                data = json.load(f)
                for key in ['article_cause_info','article_symptom_info','article_prevent_info','article_inspect_info','article_treat_info']:
                    _list = data.get(key,{})
                    for _dic in _list:
                        article_url = _dic.get('article_url','')
                        if not article_url:continue

                        self.dis_articles.add(article_url)
        print(len(self.dis_articles))
        self._save_article(list(self.dis_articles),self.disarticlepkl)


    def _department_article_spider(self, url):
        '''科室栏文章'''
        html = self.get_html(url)
        selector = etree.HTML(html) # class ="fl drug-pic bor mr10"
        title = selector.xpath('//div[contains(@class,"article_title pb10")]/h3/text()')[0]
        sources = selector.xpath('//div[contains(@class,"article_title pb10")]/div/span[contains(@class,"fl gray pr2")]/text()')

        category = selector.xpath('//div[contains(@class,"breadcast f12")]/a/text()')

        contents = selector.xpath('//div[contains(@class,"passage pl10 pr10 f14")]/p//text()')
        html_content = etree.tostring(selector.xpath('//div[contains(@class,"passage pl10 pr10 f14")]')[0],encoding='utf8').decode()

        relates = []
        ps = selector.xpath('//ul[@class="f14 common_list deepgray-a pt10"]/li')
        for p in ps:
            relate_url = p.xpath('./a/@href')[0]
            relate_title = p.xpath('./a/text()')[0]
            relates.append({'title':relate_title,'url':relate_url})

        _dic = {'title':title,'sources':sources,'category':category,'contents':contents,'html_content':html_content,'relates':relates}
        return _dic

    def _z_article_spider(self, url):
        '''专家栏文章'''
        html = self.get_html(url)
        selector = etree.HTML(html) # class ="fl drug-pic bor mr10"
        title = selector.xpath('//div[contains(@class,"new_artitle tc pt10")]/h3/text()')[0]
        sources = selector.xpath('//div[contains(@class,"new_artitle tc pt10")]/div/p//text()')
        category = selector.xpath('//div[contains(@class,"fl deepgray-a")]/a/text()')
        contents = selector.xpath('//div[contains(@class,"new_artcont pt10 f14 lh180 clearfix")]/p//text()')
        html_content = etree.tostring(selector.xpath('//div[contains(@class,"new_artcont pt10 f14 lh180 clearfix")]')[0],encoding='utf8').decode()

        relates = []
        ps = selector.xpath('//ul[@class="f14")]/li')
        for p in ps:
            relate_url = p.xpath('./a/@href')[0]
            relate_title = p.xpath('./a/text()')[0]
            relates.append({'title': relate_title, 'url': relate_url})

        _dic = {'title': title, 'sources': sources, 'category': category, 'contents': contents,
                'html_content': html_content, 'relates': relates}
        return _dic

    def _health_article_spider(self, url):
        '''健康百科文章'''
        html = self.get_html(url,'gbk')
        selector = etree.HTML(html) # class ="fl drug-pic bor mr10"
        title = selector.xpath('//div[contains(@class,"entry")]/h1/text()')

        sources = selector.xpath('//div[contains(@class,"entry")]/ul/li/text()')
        category = selector.xpath('//div[contains(@class,"position dep-linkb")]/a/text()')

        contents = selector.xpath('//div[contains(@class,"artical")]/p//text()')
        html_content = etree.tostring(selector.xpath('//div[contains(@class,"artical")]')[0],encoding='utf8').decode()
        relates = []

        page_ps = selector.xpath('//div[@class="page"]/ul/li')
        if len(page_ps)>3:
            print('多页：',url)
            for _p in page_ps[1:-2]:
                next_url = _p.xpath('./a/@href')[0].strip()
                html = self.get_html(next_url)
                selector = etree.HTML(html)
                next_contents = selector.xpath('//div[contains(@class,"artical")]/p//text()')
                next_html_content = etree.tostring(selector.xpath('//div[contains(@class,"artical")]')[0],
                                              encoding='utf8').decode()

                contents.extend(next_contents)
                html_content += '@@@next_page@@@'+next_html_content


        _dic = {'title': title, 'sources': sources, 'category': category, 'contents': contents,
                'html_content': html_content, 'relates': relates}
        return _dic

    def _health_article_spider2(self, url):
        '''健康百科-资讯'''



        html = self.get_html(url, 'gbk')
        selector = etree.HTML(html)  # class ="fl drug-pic bor mr10"
        title = selector.xpath('//div[@class ="article_title pb10"]/h3/text()')

        sources = []
        category = selector.xpath('//div[@class="breadcast f12"]//text()')

        contents = selector.xpath('//div[@class="passage pl10 pr10 f14"]/p//text()')
        html_content = etree.tostring(selector.xpath('//div[contains(@class,"passage pl10 pr10 f14")]')[0], encoding='utf8').decode()
        relates = []

        _dic = {'title': title, 'sources': sources, 'category': category, 'contents': contents,
                'html_content': html_content, 'relates': relates}
        return _dic

    def health_spider_main2(self):
        '''健康类文章爬取'''
        base_url = 'http://www.xywy.com'
        for page in range(1, 27):
            page_url = base_url+'/n_map/p_%s'%page
            try:
                html = self.get_html(page_url)
                selector = etree.HTML(html)
                ps = selector.xpath('//ul/li')
                for p in ps:
                    date_url = base_url + p.xpath('./a/@href')[0].strip()
                    try:

                        date = p.xpath('./a/text()')[0].strip('[] \t\n\r')

                        html = self.get_html(date_url)
                        selector = etree.HTML(html)

                        date_subs = selector.xpath('//td/span')
                        if len(date_subs)>1:
                            sub_pages = int(re.findall('\d+',date_subs[1].text)[0])
                        else:
                            sub_pages = 1

                        print(date,'包含页数：',sub_pages)

                        for sub_page in range(1,sub_pages+1):
                            date_url_n = date_url+'/%s'%sub_page
                            try:
                                if sub_page>1:
                                    html = self.get_html(date_url_n)
                                    selector = etree.HTML(html)
                                ls = selector.xpath('//div[@class="club_dic"]')
                                j = 0
                                for l in ls:
                                    label = l.xpath('./h4/var/a/text()')[0]
                                    label_url = l.xpath('./h4/var/a/@href')[0]
                                    article_url = l.xpath('./h4/em/a/@href')[0].strip()
                                    article_title = l.xpath('./h4/em/a/text()')[0]
                                    desc = l.xpath('./div/p/text()')[0]

                                    if article_url in self.articles:continue

                                    _m_dic = {'label': label, 'label_url': label_url, 'article_title': article_title,
                                              'article_url': article_url, 'desc': desc}
                                    try:
                                        _dic = self._health_article_spider(article_url)
                                        self.articles.add(article_url)
                                    except Exception as e:
                                        _dic = {}
                                        print('error:%s'%e)

                                    _m_dic.update(_dic)
                                    j += 1
                                    print(page,date,sub_page,j,article_url)

                                    with open('article_data/%s_%s_%s.json' % (date,sub_page,j), 'w') as sf:
                                        json.dump(_m_dic, sf, ensure_ascii=False, indent=4)
                            except:
                                print('error2:',date_url_n)
                                pass
                    except:
                        print('error1:',date_url)
                        pass
            except:
                print('error0:',page_url)
                pass


    def health_spider_a_date(self,date):
        base_url = 'http://www.xywy.com'
        date_url = base_url + '/n_map/list_%s' % date
        try:
            html = self.get_html(date_url)
            selector = etree.HTML(html)

            date_subs = selector.xpath('//td/span')
            if len(date_subs) > 1:
                sub_pages = int(re.findall('\d+', date_subs[1].text)[0])
            else:
                sub_pages = 1

            print(date, '包含页数：', sub_pages)

            for sub_page in range(1, sub_pages + 1):
                date_url_n = date_url + '/%s' % sub_page
                try:
                    if sub_page > 1:
                        html = self.get_html(date_url_n)
                        selector = etree.HTML(html)
                    ls = selector.xpath('//div[@class="club_dic"]')
                    j = 0
                    for l in ls:
                        try:
                            label = l.xpath('./h4/var/a/text()')[0]
                            label_url = l.xpath('./h4/var/a/@href')[0]
                            article_url = l.xpath('./h4/em/a/@href')[0].strip()
                            article_title = l.xpath('./h4/em/a/text()')[0]
                            desc = l.xpath('./div/p/text()')

                            desc = desc[0] if desc else ''

                            if article_url in self.articles: continue

                            _m_dic = {'label': label, 'label_url': label_url, 'article_title': article_title,
                                      'article_url': article_url, 'desc': desc}
                            try:
                                _dic = self._health_article_spider(article_url)
                                self.articles.add(article_url)
                            except Exception as e:
                                try:
                                    _dic = self._health_article_spider2(article_url)
                                except:
                                    _dic = {}
                                    print('error health2:%s' % e)
                                print('error:%s' % e)

                            _m_dic.update(_dic)
                            j += 1
                            print(date, sub_page, j, article_url)

                            with open('article_data/%s_%s_%s.json' % (date, sub_page, j), 'w') as sf:
                                json.dump(_m_dic, sf, ensure_ascii=False, indent=4)
                        except:
                            print('error3:', date_url_n)
                            continue
                except:
                    print('error2:', date_url_n)
                    pass
        except:
            print('error1:', date_url)
            pass

    def health_spider_main(self,start_date,end_date):
        '''健康类文章爬取'''
        base_url = 'http://www.xywy.com'
        dates = self._getStartEndday(start_date,end_date)
        for date in dates:
            self.health_spider_a_date(date)

        return dates




    def dis_article_spider_main(self):
        '''疾病关联文章推荐递归爬取'''

        def _article_recurrence_spider(article_url,k):

            try:
                if not article_url:
                    return
                if article_url in self.dis_done_articles:
                    print('url existed,pass')
                    return

                if article_url.startswith('http://www.xywy.com') or article_url.startswith('http://news.xywy.com'):
                    _art_dic = self._health_article_spider(article_url)
                    print('健康百科文章')
                elif article_url.startswith('http://z.xywy.com'):
                    _art_dic = self._z_article_spider(article_url)
                    print('专家频道文章')
                else:
                    _art_dic = self._department_article_spider(article_url)

                _art_dic.update({'article_url':article_url})
                name = article_url.replace('/','%')
                with open('dis_article_data/%s.json' % name, 'w') as sf:
                    json.dump(_art_dic, sf, ensure_ascii=False, indent=4)
                    self.dis_done_articles.add(article_url)
                print(k, article_url)
                if len(self.dis_done_articles)%100==0:
                    self._save_article(list(self.dis_done_articles),self.disdonearticlepkl)

                p = k+1
                if k > 2:  # 递归深度2层
                    return
                relates = _art_dic.get('relates', [])
                for relate_dic in relates:
                    relate_url = relate_dic.get('url', '')
                    _article_recurrence_spider(relate_url, p)
            except:
                self._save_article(list(self.dis_done_articles), self.disdonearticlepkl)
                return

        for article_url in self.dis_articles:
            _article_recurrence_spider(article_url, 0)


json.dump()




asp = ArticleSpider()
# asp.load_model()
asp.get_ip('ips.json')
#asp.health_spider_main('2013-03-01','2014-03-01')
# asp._load_dis_articles('/Users/macpro/Documents/工作记录/词表搜集/medical_kg/disease_data')
# asp.dis_article_spider_main()

import sys
for line in sys.stdin:
    line = line.strip()
    print('start date:',line)
    asp.health_spider_a_date(line)

