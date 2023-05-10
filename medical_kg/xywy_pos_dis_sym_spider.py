#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xywy_pos_dis_sym_spider.py
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
class PosDisSymSpider(XywySpider):
    def __init__(self):
        super(PosDisSymSpider, self).__init__()

        # self.load_model()

    def spider_main(self):
        _list_map = {'bi':'鼻','er':'耳','yan':'眼','kou':'口','jingbu':'颈部',
                 'xiazhi':'下肢','shangzhi':'上肢','xiongbu':'胸部',
                 'fubu':'腹部','yaobu':'腰部','nvxingpengu':'女性盆骨',
                 'nanxinggugou':'男性盆骨','pifu':'皮肤','quanshen':'全身',
                 'paixiebuwei':'排泄部位'}
        for page in _list_map:
            try:
                disurl = 'http://jib.xywy.com/html/%s.html'%page
                data = {}
                data['url'] = disurl
                data['pos'] = _list_map[page]
                data['result'] = self.pos_dis_sym_spider(disurl)
                print(page, disurl, 'done')
                with open('pos_dis/%s.json'%page, 'w') as sf:
                    json.dump(data, sf, ensure_ascii=False,indent=4)

                symurl = 'http://zzk.xywy.com/p/%s.html' % page
                data = {}
                data['url'] = symurl
                data['pos'] = _list_map[page]
                data['result'] = self.pos_dis_sym_spider(symurl)
                print(page, symurl, 'done')
                with open('pos_sym/%s.json' % page, 'w') as sf:
                    json.dump(data, sf, ensure_ascii=False, indent=4)

            except Exception as e:
                print(e, page)
        return

    '''页面解析'''
    def pos_dis_sym_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)

        cj_items = []
        cj_ls = selector.xpath('//div[@class="jblist-bd bor"]//ul[@class="ks-ill-list clearfix mt10"]/li')
        for li in cj_ls:
            name = li.xpath('a/@title')[0]
            name_url = li.xpath('a/@href')[0]
            _dic={}
            _dic['name'] = name
            _dic['url'] = name_url
            cj_items.append(_dic)

        other_items = []
        other_ls = selector.xpath('//div[@class="jblist-bd bor mt10 pr"]//ul[@class="ks-ill-list clearfix mt10"]/li')
        for li in other_ls:
            name = li.xpath('a/@title')[0]
            name_url = li.xpath('a/@href')[0]
            _dic={}
            _dic['name'] = name
            _dic['url'] = name_url
            other_items.append(_dic)

        _data = {}
        _data['cj_items'] = cj_items
        _data['other_items'] = other_items

        return _data

if __name__=="__main__":

    msp = PosDisSymSpider()
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