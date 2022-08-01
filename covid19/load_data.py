#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     load_data.py.py
# author:   zlw2008ok@126.com
# date:     2022/7/30
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import time
import requests
import json
import xlwt
def get_time(fmt:str='%Y-%m-%d %H-%M-%S') -> str:
    '''
    获取当前时间:%Y-%m-%d %H-%M-%S
    '''
    ts = time.time()
    ta = time.localtime(ts)
    t = time.strftime(fmt, ta)
    return t


map1 = {"times": "截止时间1", #"截至7月30日17时30分",
        "mtime": "截止时间2", # "2022-07-30 17:30:00",
        "cachetime": "缓存时间", #"2022-07-30 17:59:06",
        "ispub": "是否公开", # true,
        "gntotal": "累计确诊", # "5130275",
        "deathtotal": "累计死亡", # "23563",
        # "sustotal": "", # "1",
        "curetotal": "累计治愈", # "304208",
        "locIncrNum": "现存本土确诊", # "1214",
        "localExistingNum": "现存本土确诊", # "1214",
        "econNum": "现存确诊", # "4802504",
        "heconNum": "现存重症", # "11",
        "asymptomNum": "现存无症状", # "7136",
        "jwsrNum": "累计境外输入", # "20633",
        # "contactNum": "", # "131465",
        "localconNum": "新增本土确诊", # "49",
        "addAsymNum": "新增无症状", # "348",
        }

res = requests.get('https://news.sina.com.cn/project/fymap/ncp2020_full_data.json')
res_str = res.text.replace('jsoncallback(','').strip(');')
data = json.loads(res_str).get('data',{})
suffix = get_time('%Y_%m_%d:%H')
savefile =f"sina_covid19_data_{suffix}.xlsx"

# with open('sina_ncp2020_full_data.json','r') as f:
#     _data = json.load(f)
#     data = _data.get('data',{})

workbook=xlwt.Workbook()

# 全国
worksheet = workbook.add_sheet("全国(含港澳台)数据统计")
j = 0
for key in data:
    value = data[key]
    if isinstance(value, (list,dict)):
        pass
    else:
        value = str(value)
        worksheet.write(0, j, key)
        worksheet.write(1, j, map1.get(key,key))
        worksheet.write(2, j, value)
        j += 1

# 每日
key1 = 'add_daily'
temp_dic = data.get(key1,{})
worksheet = workbook.add_sheet("今日增减")
j = 0
for key in temp_dic:
    value = temp_dic[key]
    value = str(value)
    worksheet.write(0, j, key)
    worksheet.write(2, j, value)
    j += 1

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

# top
key1 = 'jwsrTop'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("境外输入Top")
parser(worksheet,temp_list)

# locIncrProTop
key1 = 'locIncrProTop'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("现存本土省份Top")
parser(worksheet,temp_list)

# list
key1 = 'list'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("31省市区情况")
parser(worksheet,temp_list)

# highAndMiddle
key1 = 'highAndMiddle'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("中高风险地区")
parser(worksheet,temp_list)

# historylist
key1 = 'historylist'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("国内历史记录")
parser(worksheet,temp_list)

# otherlist
key1 = 'otherlist'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("国外情况")
parser(worksheet,temp_list)

# otherhistorylist
key1 = 'otherhistorylist'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("国外历史记录")
parser(worksheet,temp_list)

# worldlist
key1 = 'worldlist'
temp_list = data.get(key1,[])
worksheet = workbook.add_sheet("世界情况")
parser(worksheet,temp_list)

workbook.save(savefile)
