#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xywy_inspect_spider.py
# author:   zlw2008ok@126.com
# date:     2023/1/30
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import re
import json
import os
from lxml import etree
import xml.etree.ElementTree as eTree2
from xywy_spider import XywySpider



'''xywy.com'''
class InspectSpider(XywySpider):
    def __init__(self):
        super(InspectSpider, self).__init__()
        self.food_set = set()
        self.drug_set = set()
        self.foodpkl = 'food.json'
        self.drugpkl = 'drug.json'
        # self.load_model()

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
        for page in range(1, 3782):
            try:
                inspect_url = 'http://jck.xywy.com/jc_%s.html'%page
                data = {}
                data['url'] = inspect_url
                print('inspectinfo...')
                data['result'] = self.basicinfo_spider(inspect_url)

                print(page, inspect_url, 'done')
                with open('inspect_data/%s.json'%page, 'w') as sf:
                    json.dump(data, sf, ensure_ascii=False,indent=4)

            except Exception as e:
                print(e, page)
        return

    '''页面解析'''
    def basicinfo_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        title = selector.xpath('//title/text()')[0]

        category = selector.xpath('//div[@class="headings f12 fYaHei gray-a mt10"]/a/text()')
        desc = selector.xpath('//div[@class="baby-weeks"]/p/text()')

        options = selector.xpath('//div[@class="baby-target ops-content"]/div')
        base_dic = {}
        dn = len(options)
        if dn ==2:
            others = options[1].xpath('./div')
        else:
            others = options[2:]
        base_name = options[0].xpath('text()')[0]
        base_ps1 = options[1].xpath('./p')
        base_items = []
        for sp in base_ps1:
            for _p in sp.xpath('./span'):
                item = _p.xpath('string(.)')
                base_items.append(item)
        base_ps2 = options[1].xpath('./div')
        for _p in base_ps2:
            item = _p.xpath('string(.)')
            base_items.append(item)

        base_dic[base_name] = base_items
        other_dic = {}
        subn = len(others)
        for i in range(0,subn,2):
            other_name = others[i].xpath('text()')[0]
            other_string = others[i+1].xpath('string(.)')
            # other_html = etree.tostring(others[i+1],method='xml',encoding='utf8').decode()
            other_html = eTree2.tostring(others[i+1],encoding='utf8').decode()
            other_dic[other_name] = [other_string,other_html]

            data = re.findall('结果.{0,5}可能.{0,2}疾病[\s\S]+$',other_string)
            if data:
                other_dic['可能的疾病'] = data[0]


        releate_dic = {}
        releates = selector.xpath('//div[@class="items-right-site fr"]/div')
        for ul in releates:
            aa=ul.xpath('./div')
            if len(aa)>1:
                releate_name = aa[0].xpath('text()')[0]
                releate_items = []
                for li in aa[1].xpath('./ul/li'):
                    _item = li.xpath('a/@title')[0]
                    releate_items.append(_item)
                releate_dic[releate_name] = releate_items

        basic_data = {}
        basic_data['title'] = title.split('结果分析')[0]
        basic_data['category'] = category
        basic_data['desc'] = desc
        basic_data['base_infos'] = base_dic
        basic_data['other_infos'] = other_dic
        basic_data['releate_infos'] = releate_dic
        return basic_data

if __name__=="__main__":

    msp = InspectSpider()
    msp.get_ip('ips.json')

    # url = 'http://jib.xywy.com/il_sii/article_cause/1034.htm'
    # url = 'http://z.xywy.com/doc/lfxwj/wenzhang/83-26525.htm'  # 专家文章
    # url = 'http://pfxbk.xywy.com/qb/by/../arc924551.html'
    # html = msp.get_html(url)
    # selector = etree.HTML(html)
    # title = selector.xpath('//title/text()')
    # print(title)
    # result = msp.article_spider(url)
    # print(result)


    #
    # image_url = 'http://static.i3.xywy.com/cms/caipu/uplode/1384505705443.jpg'
    # msp.save_image(image_url,'aaa.jpg')

    msp.spider_main()