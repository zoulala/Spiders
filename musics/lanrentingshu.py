#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     lanrentingshu.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-08-07
# brief:    
#
# cmd>e.g:  
# *****************************************************

##http://www.lrts.me/index


# coding: utf-8
# http://30daydo.com
import urllib

import os
import requests
import time
from lxml import etree


def spider():
    curr=os.getcwd()
    target_dir=os.path.join(curr,'data')
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    for i in range(1, 100, 10):
        url = 'http://www.lrts.me/playlist'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        s = requests.get(url=url, headers=headers)
        tree = etree.HTML(s.text)
        nodes = tree.xpath('//*[starts-with(@class,"clearfix section-item section")]')
        print (len(nodes))
        for node in nodes:
            filename = node.xpath('.//div[@class="column1 nowrap"]/span/text()')[0]
            link = node.xpath('.//input[@name="source" and @type="hidden"]/@value')[0]

            print(link)
            post_fix=link.split('.')[-1]
            full_path= filename+'.'+post_fix
            urllib.urlretrieve(link, filename=os.path.join(target_dir,full_path))
            time.sleep(1)


if __name__ == '__main__':
    spider()