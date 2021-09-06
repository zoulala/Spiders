#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xywy_disease_spider.py
# author:   zlw2008ok@126.com
# date:     2021-07-01
# brief:    
#
# cmd>e.g:  
# *****************************************************

import json
import os
from lxml import etree
from xywy_spider import XywySpider

'''xywy.com'''
class DiseaseSpider(XywySpider):
    def __init__(self):
        super(DiseaseSpider, self).__init__()
        self.food_set = set()
        self.drug_set = set()
        self.foodpkl = 'food.json'
        self.drugpkl = 'drug.json'
        self.load_model()

    def load_model(self):
        if os.path.exists(self.foodpkl):
            with open(self.foodpkl,'r') as f:
                self.food_set = set(json.load(f))
        if os.path.exists(self.drugpkl):
            with open(self.drugpkl, 'r') as f:
                self.drug_set = set(json.load(f))

    def __del__(self):
        with open(self.foodpkl, 'w') as sf:
            json.dump(list(self.food_set), sf, ensure_ascii=False)
            print('food_set saved ')
        with open(self.drugpkl, 'w') as sf:
            json.dump(list(self.drug_set), sf, ensure_ascii=False)
            print('drug_set saved ')

    def spider_main(self):
        for page in range(1, 12000):
            try:
                basic_url = 'http://jib.xywy.com/il_sii/gaishu/%s.htm'%page  # 概述
                cause_url = 'http://jib.xywy.com/il_sii/cause/%s.htm'%page  # 诱因
                prevent_url = 'http://jib.xywy.com/il_sii/prevent/%s.htm'%page  # 预防
                neopathy_url = 'http://jib.xywy.com/il_sii/neopathy/%s.htm' % page  # 并发症

                symptom_url = 'http://jib.xywy.com/il_sii/symptom/%s.htm'%page  # 症状
                inspect_url = 'http://jib.xywy.com/il_sii/inspect/%s.htm'%page  # 检查
                diagnosis_url = 'http://jib.xywy.com/il_sii/diagnosis/%s.htm'%page  # 鉴别诊断

                treat_url = 'http://jib.xywy.com/il_sii/treat/%s.htm'%page  # 治疗
                nursing_url = 'http://jib.xywy.com/il_sii/nursing/%s.htm'%page  # 护理
                food_url = 'http://jib.xywy.com/il_sii/food/%s.htm'%page  # 饮食保健
                drug_url = 'http://jib.xywy.com/il_sii/drug/%s.htm'%page  # 好评药品

                article_cause_url = 'http://jib.xywy.com/il_sii/article_cause/%s.htm'%page  # 相关文章-病因
                article_symptom_url = 'http://jib.xywy.com/il_sii/article_symptom/%s.htm'%page  # 相关文章-症状
                article_prevent_url = 'http://jib.xywy.com/il_sii/article_prevent/%s.htm'%page  # 相关文章-预防
                article_inspect_url = 'http://jib.xywy.com/il_sii/article_inspect/%s.htm'%page  # 相关文章-检查
                article_treat_url = 'http://jib.xywy.com/il_sii/article_treat/%s.htm'%page  # 相关文章-治疗

                data = {}
                data['url'] = basic_url
                print('basicinfo...')
                data['basic_info'] = self.basicinfo_spider(basic_url)
                print('cause_info...')
                data['cause_info'] =  self.common_spider(cause_url)
                print('prevent_info...')
                data['prevent_info'] =  self.common_spider(prevent_url)
                print('neopathy_info...')
                data['neopathy_info'] = self.neopathy_spider(neopathy_url)

                print('symptom_info...')
                data['symptom_info'] = self.common_spider(symptom_url)
                print('inspect_info...')
                data['inspect_info'] = self.common_spider(inspect_url)
                print('diagnosis_info...')
                data['diagnosis_info'] = self.common_spider(diagnosis_url)

                print('treat_info...')
                data['treat_info'] = self.common_spider(treat_url)
                print('nursing_info...')
                data['nursing_info'] = self.common_spider(nursing_url)
                print('food_info...')
                data['food_info'] = self.food_spider(food_url)
                print('drug_info...')
                data['drug_info'] = self.drug_spider(drug_url)

                print('article_cause_info...')
                data['article_cause_info'] = self.article_spider(article_cause_url)
                print('article_symptom_info...')
                data['article_symptom_info'] = self.article_spider(article_symptom_url)
                print('article_prevent_info...')
                data['article_prevent_info'] = self.article_spider(article_prevent_url)
                print('article_inspect_info...')
                data['article_inspect_info'] = self.article_spider(article_inspect_url)
                print('article_treat_info...')
                data['article_treat_info'] = self.article_spider(article_treat_url)

                print(page, basic_url)

                with open('disease_data/%s.json'%page, 'w') as sf:
                    json.dump(data, sf, ensure_ascii=False,indent=4)

            except Exception as e:
                print(e, page)
        return

    '''基本信息解析'''
    def basicinfo_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        title = selector.xpath('//title/text()')[0]
        category = selector.xpath('//div[@class="wrap mt10 nav-bar"]/a/text()')
        desc = selector.xpath('//div[@class="jib-articl-con jib-lh-articl"]/p/text()')

        infobox = []
        strongs = selector.xpath('//div[@class="mt20 articl-know"]')
        for sts in strongs:
            strong_title = sts.xpath('strong/text()')[0]
            ps = sts.xpath('p')
            for p in ps:
                # key = p.xpath('./span[@class="tr txt-left fl"]/text()')[0]
                # values = p.xpath('./span[@class="fl txt-right"]/text()')
                spans = p.xpath('./span')
                if not spans:
                    p_values = p.text
                    p_name = strong_title
                else:
                    p_name = spans[0].text
                    p_values = spans[1].xpath('string(.)').split()
                _dic = {'p_name':p_name,'p_values':p_values,'p_label':strong_title}
                infobox.append(_dic)

        # ps = selector.xpath('//div[@class="mt20 articl-know"]/p')
        # infobox = []
        # for p in ps:
        #     info = p.xpath('string(.)')
        #     # info = p.xpath('string(.)').replace('\r','').replace('\n','').replace('\xa0', '').replace('   ', '').replace('\t','')
        #     infobox.append(info)

        basic_data = {}
        basic_data['category'] = category
        basic_data['name'] = title.split('的简介')[0]
        basic_data['desc'] = desc
        basic_data['attributes'] = infobox

        return basic_data


    '''通用解析模块'''
    def common_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)

        # ps = selector.xpath('//div[@class =" jib-articl fr f14 jib-lh-articl"]')[0].xpath('.//p|.//strong|.//h3')
        ps = selector.xpath('//div[@class =" jib-articl fr f14 jib-lh-articl"]/*|//div[@class ="jib-articl fr f14 jib-lh-articl"]/*')
        # ps2 = selector.xpath('string(//div[@class =" jib-articl fr f14 jib-lh-articl"])')

        infobox = []
        for p in ps:
            tag = '<'+p.tag+'>'
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ','').replace('\t', '')
            if info:
                infobox.append(tag+info)

        return '\n'.join(infobox)

    '''并发症解析模块'''
    def neopathy_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        neopathy = selector.xpath('//span[@class="db f12 lh240 mb15 "]//text()')
        ps = selector.xpath('//div[@class =" jib-articl fr f14 jib-lh-articl"]/*|//div[@class ="jib-articl fr f14 jib-lh-articl"]/*')

        infobox = []
        for p in ps:
            tag = '<' + p.tag + '>'
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ','').replace('\t', '')
            if info:
                infobox.append(tag+info)
        _dic = {"neopathy":neopathy,"context":'\n'.join(infobox)}

        return _dic

    '''治疗解析模块'''
    def treat_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)

        common = []  # 治疗常识
        strongs = selector.xpath('//div[@class="mt20 articl-know"]')
        for sts in strongs:
            strong_title = sts.xpath('strong/text()')[0]
            ps = sts.xpath('p')
            for p in ps:
                # key = p.xpath('./span[@class="tr txt-left fl"]/text()')[0]
                # values = p.xpath('./span[@class="fl txt-right"]/text()')
                spans = p.xpath('./span')
                if not spans:
                    p_values = p.text
                    p_name = strong_title
                else:
                    p_name = spans[0].text
                    p_values = spans[1].xpath('string(.)').split()
                _dic = {'p_name':p_name,'p_values':p_values,'p_label':strong_title}
                common.append(_dic)

        ps = selector.xpath('//div[@class="jib-lh-articl"]/*')
        infobox = []
        for p in ps:
            tag = '<' + p.tag + '>'
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ','').replace('\t', '')
            if info:
                infobox.append(tag+info)

        _dic = {"treat_attributes": common, "context": '\n'.join(infobox)}

        return _dic

    '''food治疗解析'''
    def food_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)

        def _food(ps):
            _dic = {}
            sps = ps.xpath('./div')
            if not sps:
                return {}

            foods = []
            content = ''
            if len(sps) > 1:
                content = sps[0].xpath('string(.)').strip()
                for sp in sps[1].xpath('./*'):
                    food_url = sp.xpath('.//a/@href')[0].strip()
                    img_url = sp.xpath('.//img/@src')[0].strip()
                    food_name = sp.xpath('.//p/text()')[0].strip()
                    sub_dic = {'food_name': food_name, 'img_url': img_url,
                               'food_url': food_url}
                    foods.append(sub_dic)
                    if food_name not in self.food_set:
                        self.save_image(img_url, food_name,'./food_imgs')
                        self.food_set.add(food_name)
            else:
                content = sps[0].xpath('string(.)').strip()

            _dic['foods'] = foods
            _dic['content'] = content
            return _dic

        divs = selector.xpath('//div[@class="jib-diet-tab"]/div')
        try:
            titles = divs[0].xpath('.//li/text()')
            # titles = ['饮食保健','宜吃食物','忌吃食物','推荐食谱']

            food_data = {}
            ps = divs[1].xpath('./div')
            food_data['饮食保健'] = ps[0].xpath('string(.)').strip()
            food_data['宜吃食物'] = _food(ps[1])
            food_data['忌吃食物'] = _food(ps[2])
            food_data['推荐食谱'] = _food(ps[3])

        except:
            return {}

        return food_data

    '''好评药品解析'''
    def drug_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html) # class ="fl drug-pic bor mr10"

        drug_data = []
        divs = selector.xpath('//div[starts-with(@class,"city-drugbox") and contains(@class,"bor-dash")]')
        for div in divs:
            try:
                _dic = {}
                sps = div.xpath('./div')
                if not sps:
                    return {}

                drug_url = sps[0].xpath('.//a/@href')[0].strip()
                img_url = sps[0].xpath('.//img/@src')[0].strip()

                drug_div = sps[1].xpath('.//p')
                drug_name = drug_div[0].xpath('string(.)').strip()
                price = drug_div[1].xpath('string(.)').strip()
                effect = drug_div[2].xpath('string(.)').strip()
                _dic = {'drug_url': drug_url, 'img_url': img_url,
                        'drug_name': drug_name, 'price': price, 'effect': effect}
                drug_data.append(_dic)

                if drug_url not in self.drug_set:
                    self.save_image(img_url, drug_name, './drug_imgs')
                    self.drug_set.add(drug_url)
            except:
                continue
        return drug_data

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


    '''相关文章'''
    def article_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html) # class ="fl drug-pic bor mr10"
        ps = selector.xpath('//div[contains(@class,"jib-expert-articl fr")]/div')
        relate_articles = []
        k = 0
        for p in ps:
            sub_ps = p.xpath('./p')
            article_url = sub_ps[0].xpath('./a/@href')[0].strip()
            article_title = sub_ps[0].xpath('./a/text()')[0].strip()
            if not article_url.startswith('http'):continue

            print(k)
            k+=1
            # continue
            _dic = {'article_title': article_title, 'article_url': article_url}
            try:
                if article_url.startswith('http://www.xywy.com') or article_url.startswith('http://news.xywy.com'):
                    _art_dic= self._health_article_spider(article_url)
                    print('健康百科文章')
                elif article_url.startswith('http://z.xywy.com'):
                    _art_dic = self._z_article_spider(article_url)
                    print('专家频道文章')
                else:
                    _art_dic = self._department_article_spider(article_url)
            except:
                relate_articles.append(_dic)
                continue
            _dic.update(_art_dic)
            relate_articles.append(_dic)

        return relate_articles


if __name__=="__main__":

    msp = DiseaseSpider()
    msp.get_ip('ips.json')

    url = 'http://jib.xywy.com/il_sii/article_cause/1034.htm'
    # url = 'http://z.xywy.com/doc/lfxwj/wenzhang/83-26525.htm'  # 专家文章
    # url = 'http://pfxbk.xywy.com/qb/by/../arc924551.html'
    # html = msp.get_html(url)
    # selector = etree.HTML(html)
    # title = selector.xpath('//title/text()')
    # print(title)
    result = msp.article_spider(url)
    print(result)


    #
    # image_url = 'http://static.i3.xywy.com/cms/caipu/uplode/1384505705443.jpg'
    # msp.save_image(image_url,'aaa.jpg')

    # msp.spider_main()