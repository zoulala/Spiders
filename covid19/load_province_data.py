#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     load_province_data.py
# author:   zlw2008ok@126.com
# date:     2022/8/3
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import requests
import json
import xlwt
import time
import random

# province = "beijing"
# url = 'https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=province&province=%s'% province

savefile = "sina_covid19_provinces_history_data.xlsx"
savefile2 = "sina_covid19_cities_history_data.xlsx"
workbook=xlwt.Workbook()
workbook2=xlwt.Workbook()
provinces = ["beijing","shanghai","tianjin","shenzhen","hebei","heilongjiang","liaoning","jilin","jiangsu","zhejiang","shandong","henan","shanxi",
             "shanxis","gansu","qinghai","xinjiang","xizang","sichuan","guizhou","yunnan","guangxi","guangdong","hunan","hubei",
             "jiangxi","anhui","fujian","xianggang","aomen","hainan","taiwan","chongqing"]
def parser(worksheet,temp_list):
    i = 1
    keys = dict([(k, xi) for xi, k in enumerate(temp_list[0].keys())])
    for _temp_dic in temp_list:
        for key2 in _temp_dic:
            if key2 not in keys:
                ln = len(keys.keys())
                keys[key2] = ln
            value = _temp_dic[key2]
            if isinstance(value, (list, dict)):
                value = json.dumps(value, ensure_ascii=False)
            else:
                value = str(value)
            worksheet.write(i, keys[key2], value)
        i += 1
    for key2 in keys:
        xi = keys[key2]
        worksheet.write(0, xi, key2)

# 全国
for province in provinces:
    try:
        url = 'https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=province&province=%s'% province
        res = requests.get(url)
        res_str = res.text
        data = json.loads(res_str).get('data', {})

        province_name = data.get('province','')
        print(province_name)
        historylist = data.get('historylist',[])
        worksheet = workbook.add_sheet(province_name)
        parser(worksheet, historylist)


        citys = data.get('city',[])
        for _city in citys:
            city=''
            try:
                citycode = _city.get('citycode','')
                url = 'https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=city&citycode=%s' % citycode
                res = requests.get(url)
                res_str = res.text
                data = json.loads(res_str).get('data', {})
                city = data.get('city','')
                print(city)
                historylist = data.get('historylist', [])
                worksheet = workbook2.add_sheet(province_name+'_'+city)
                parser(worksheet, historylist)
                time.sleep(random.randint(3,9))
            except:
                print('city error',city)
                time.sleep(random.randint(1, 3))
                continue

        time.sleep(random.randint(3,9))
    except:
        print('error',province)
        time.sleep(random.randint(1, 3))
        continue

workbook.save(savefile)
workbook2.save(savefile2)

