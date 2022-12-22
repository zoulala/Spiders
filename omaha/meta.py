#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     meta.py
# author:   zlw2008ok@126.com
# date:     2022/10/21
# desc:     获取数据元详细信息
#
# cmd>e.g.:  
# *****************************************************


import json
import requests


url = "https://hita.omaha.org.cn/resource/mdDetailJson"
data = {
"hitaId": "H20001",
"metadataType": "值域"
}

simulateBrowserData = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Content-Length": "45",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "identitys=4; grading=4; Hm_lvt_c5f999fb6da6b6ecd0233092b251f516=1652840057; Hm_lpvt_c5f999fb6da6b6ecd0233092b251f516=1652840057; member_UU=0381f598-201f-4335-8597-72f4aedd00a8; member_UN=qihl@xnewtech.com; identitys=4; grading=4; JSESSIONID=7c13883e-b073-4dfa-8e6b-95df4f266250",
        "Host": "hita.omaha.org.cn",
        "Origin": "https://hita.omaha.org.cn",
        # "Referer": "https://hita.omaha.org.cn/resource/mdDetail?hitaId=H20001&metadataType=%E5%80%BC%E5%9F%9F&type=1&userDefined=1&num=201",
        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
}


response = requests.post(url, data=data, headers=simulateBrowserData)
print(response.text)


