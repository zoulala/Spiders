#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     zlwtest.py
# author:   zlw2008ok@126.com
# date:     2022/12/22
# desc:     
#
# cmd>e.g.:  
# *****************************************************
import json
import requests
import execjs   # pip3 install pyexecjs2

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "69",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "vipapi.qimingpian.cn",
    "Origin": "https://www.qimingpian.com",
    "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }

data = {
    "time_interval": "",
    "tag": "",
    "tag_type": "",
    "province": "",
    "lunci": "",
    "page": 1,
    "num": 20,
    "unionid": "",
    }

res = requests.post(url,data=data,headers=headers)
res_str = res.text
res_json = json.loads(res_str)  #res.json()
encrypt_data = res_json.get('encrypt_data', "")

print(encrypt_data)
decode_data = execjs.compile(open("example.js",'r',encoding='utf-8').read()).call('s', encrypt_data)

print(decode_data)

