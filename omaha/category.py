#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     category.py
# author:   zlw2008ok@126.com
# date:     2022/10/21
# desc:     信息标准文件--爬取标签
#
# cmd>e.g.:  
# *****************************************************
import time
import requests
import json
sf = open('information_standard_file_labels.txt','w')
for page in range(1,45):
    url = "https://hita.omaha.org.cn/sfile/sFileJson?pageNo=%s" % page


    data = requests.get(url)
    sf.write(data.text+'\n')
    # print(data.text)
    time.sleep(3)
    print(page)



