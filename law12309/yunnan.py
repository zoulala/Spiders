#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     yunnan.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-12-21
# brief:    
#
# cmd>e.g:  
# *****************************************************

import time
import json
import requests
import random
from urllib import request

class Request():
    '''Restful'''
    def __init__(self,url):
        self.url = url

    def request(self, data):
        '''post请求接口'''
        jdata = json.dumps(data).encode(encoding='utf-8')
        # print jdata
        headers = {'Content-Type': 'application/json'}  # 指明用json方式发送数据
        req = request.Request(self.url, headers=headers,data=jdata)
        response = request.urlopen(req)
        res = response.read()
        js_out = json.loads(res)
        return js_out

    def request2(self, data):
        res = requests.post(self.url, json=data)  # post请求用data参数
        # print(key)
        js_res = json.loads(res.text, encoding='utf8')
        return js_res



rq = Request(url='https://www.12309.gov.cn/getFileListByPage')

sf = open('zousi20211014.txt','w')

for page in range(1,800):

    data = {"codeId":"","page":page,"size":15,"fileType":"重要案件信息","channelWebPath":"/gj/yn","channelLevels":""}

    time.sleep(2+3*random.random())
    try:
        out = rq.request2(data)
        results = out.get('results',{})
        hits = results.get('hits',{})
        hits1 = hits.get('hits',[])
        print(page,len(hits1))
        for _dic in hits1:
            title = _dic.get('title','')
            # print(title)
            publishTime = _dic.get('publishedTimeStr','')
            subTitle = _dic.get('subTitle','')
            memo = _dic.get('memo','')
            content = _dic.get('content','')
            out_str = '。'.join([title,subTitle,memo,content])
            if '走私' in out_str:
                print(page)
                print(title)
                sf.write(str(page)+'\t'+publishTime+'\t'+out_str+'\n')
    except:
        continue
sf.close()



