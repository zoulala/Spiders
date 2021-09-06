#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xywy_qa_spider.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-07-12
# brief:
#
# cmd>e.g:  
# *****************************************************

# resource http://club.xywy.com/keshi/1.html

import re
import json
import os
from lxml import etree
from xywy_spider import XywySpider

class QaSpider(XywySpider):
    '''有问必答爬取类'''

    def __init__(self):
        super(QaSpider,self).__init__()
        self.done_urls = set()
        self.donefile = 'done_qa_urls.json'
        self.base_url = 'http://club.xywy.com'

    def _load_done_url(self):
        if os.path.exists(self.donefile):
            with open(self.donefile,'r') as f:
                self.done_urls = set(json.load(f))

    def _qa_spider(self, url):
        '''qa页面解析'''
        html = self.get_html(url,'gbk')
        selector = etree.HTML(html) # class ="fl drug-pic bor mr10"

        category = selector.xpath('//p[@class ="pt10 pb10 lh180 znblue normal-a"]/a/text()')
        title = selector.xpath('//p[@class="fl dib fb"]/@title')[0]
        sources = selector.xpath('//div[@class ="f12 graydeep Userinfo clearfix pl29"]/span/text()')
        contents = selector.xpath('//div[@class ="graydeep User_quecol pt10 mt10"]/text()')

        html_content = etree.tostring(selector.xpath('//div[contains(@class,"graydeep User_quecol pt10 mt10")]')[0],encoding='utf8').decode()

        relates = []
        lis = selector.xpath('//div[ @ id = "ulxgwtg"] / ul/li')
        for p in lis:
            relate_url = p.xpath('./a/@href')[0]
            relate_title = p.xpath('./a/text()')[0]
            relates.append({'title':relate_title,'url':relate_url})

        replays = []
        ps = selector.xpath('//div[@class="Doc_dochf  mb15 bc"]|//div[@class="Doc_dochf mb15 bc"]')
        for p in ps:
            answer = p.xpath('./div[1]//text()')
            answer_time = p.xpath('./p/span/text()')
            replays.append({'answer':answer,'answer_time':answer_time})

        relates_qa = []
        rqs = selector.xpath('//div[@class="docall relate-con  pr mt10 f12"]')
        for p in rqs:
            relate_title = p.xpath('./div[@class="relate-ques"]/a/text()')[0]
            relate_url = self.base_url + p.xpath('./div[@class="relate-ques"]/a/@href')[0]
            relate_answer = p.xpath('.//div[@class="fl relate-para"]//text()')
            relates_qa.append({'relate_title':relate_title,'relate_url':relate_url, 'relate_answer':relate_answer})

        relates_by_people = []
        rbp = selector.xpath('//ul[@class="Doc_xgqul clearfix f12 mt10 normal-a pb5"]/li')
        for p in rbp:
            relate_title = p.xpath('./a/text()')[0]
            relate_url = self.base_url +p.xpath('./a/@href')[0]
            relates_by_people.append({'relate_title':relate_title,'relate_url':relate_url })

        _dic = {'title': title, 'sources': sources, 'category': category, 'contents': contents,
                'html_content': html_content, 'relates': relates, 'replays':replays, 'relates_qa':relates_qa,'relates_by_people':relates_by_people}
        return _dic


    def qa_spider_main(self, st='2004-11-24', et='2021-01-03'):
        '''问答爬取'''
        date_list = self._getStartEndday(st,et)
        for date in date_list:
            date_url = 'http://club.xywy.com/keshi/%s/%s.html'%(date, 1)
            try:
                html = self.get_html(date_url)
                selector = etree.HTML(html)

                date_pages = selector.xpath('//div[@class="subFen"]/text()')
                if len(date_pages) > 1:
                    date_page_str = ''.join(date_pages)
                    sub_pages = int(re.findall('共.*(\d+).*页', date_page_str)[0])
                else:
                    sub_pages = 1

                print(date, '包含页数：', sub_pages)
                for sub_page in range(1,sub_pages+1):
                    date_url = 'http://club.xywy.com/keshi/%s/%s.html' % (date, sub_page)
                    try:
                        if sub_page > 1:
                            html = self.get_html(date_url)
                            selector = etree.HTML(html)
                        ls = selector.xpath('//div[@class="club_dic"]')
                        j = 0
                        for l in ls:
                            label = l.xpath('./h4/var/a/text()')[0]
                            label_url = l.xpath('./h4/var/a/@href')[0]
                            qa_url = l.xpath('./h4/em/a/@href')[0].strip()
                            qa_title = l.xpath('./h4/em/a/text()')[0]
                            desc = l.xpath('./div/p/text()')[0]

                            if qa_url in self.done_urls: continue

                            _m_dic = {'label': label, 'label_url': label_url, 'qa_title': qa_title,
                                      'qa_url': qa_url, 'desc': desc}
                            try:
                                _dic = self._qa_spider(qa_url)
                                self.done_urls.add(qa_url)
                            except Exception as e:
                                _dic = {}
                                print('error:%s' % e)

                            _m_dic.update(_dic)
                            j += 1
                            print(date, sub_page, j, qa_url)

                            with open('qa_data/%s_%s_%s.json' % (date, sub_page, j), 'w') as sf:
                                json.dump(_m_dic, sf, ensure_ascii=False, indent=4)
                    except:
                        print('error2:', date_url)
                        pass
            except:
                print('error1:', date_url)
                pass

asp = QaSpider()
asp.qa_spider_main('2004-11-24','2021-01-04')