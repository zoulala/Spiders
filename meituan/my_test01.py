#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     my_test01.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-06-03
# brief:    
#
# cmd>e.g:  
# *****************************************************

'''根据url，请求html'''
import urllib.request
import urllib.parse
import requests
from lxml import etree
import json
import xlwt

def get_html( url,city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    simulateBrowserData = {
        'Accept': '*/*',
        'Accept-Encoding': 'br, gzip, deflate',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Host': city + '.meituan.com',
        'Referer': 'https://' + city + '.meituan.com/meishi/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
    }

    res = requests.get(url, headers=simulateBrowserData,allow_redirects=False)
    return res.text
    req = urllib.request.Request(url=url, headers=simulateBrowserData)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf8')
    return html

# url = 'https://gz.meituan.com/meishi/c11b23/pn2/'
# url = 'https://nc.meituan.com/'
# url = 'https://nc.meituan.com/meishi/c11/'
# url = 'https://www.meituan.com/meishi/1165126528/'
# html = get_html(url,'nc')
#
# print(html)

def process01(filename,):
    workbook2 = xlwt.Workbook()
    sheet2 = workbook2.add_sheet("1")
    row_idx = 0
    ts = ['城市','美食代码','美食','大区域','小区域','店铺ID','店铺名','评分','评论数','人均(价格)','地址','店铺导航','电话','营业时间','推荐菜/价格','团购套餐/价格/门店价/已售']
    for i in range(len(ts)):
        title = ts[i]
        sheet2.write(row_idx, i, title)

    n = 0
    with open(filename,'r') as f:
        for line in f:
            line = line.rstrip('\n')
            data = line.split('\t')
            city, categoryID, area_name, sub_area_name, shopId, shopName, avgScore, allCommentNum, avgPrice, address, shopClass,\
            phone, openTime, shopurl,recommended, dealList = data
            recommended = json.loads(recommended)
            dealList = json.loads(dealList)

            recs = [_d['name']+' / '+str(_d['price']) for _d in recommended]
            dels = [_d['title']+' / '+str(_d['price'])+' / '+str(_d['value'])+' / '+str(_d['soldNum']) for _d in dealList]

            rec_str = '\n'.join(recs)
            del_str = '\n'.join(dels)
            print(rec_str)
            print(del_str)

            xls_outs = [city, categoryID,'蛋糕甜点' ,area_name, sub_area_name, shopId, shopName, avgScore, allCommentNum, avgPrice, address, shopClass,\
            phone, openTime,rec_str,del_str]

            row_idx += 1
            for j in range(len(xls_outs)):
                query = xls_outs[j]
                sheet2.write(row_idx, j, query)

            n +=1

            print(shopName)
            print(n)
    workbook2.save("nc_xc_shops_deal_20221219.xls")
process01('nanchang_xc_shops_0.txt')

