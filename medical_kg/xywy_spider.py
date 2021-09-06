#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xywy_spider.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-07-14
# brief:    
#
# cmd>e.g:  
# *****************************************************

import json
import os
import time
import random
import urllib.request
import urllib.parse
import requests
import datetime
from lxml import etree
# from fake_useragent import UserAgent
# import ssl
# # ssl._create_default_https_context = ssl._create_unverified_context


class XywySpider():
    def __init__(self):
        self.ip_lst = []
        self.proxy_flag = False
        # self.ua = UserAgent(verify_ssl=False)  # 通过库随机产生useragent
        # self.ua.update()
        self.user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
                         'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
                         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
                         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',


                         ]  #


    def get_ip(self,savefile):

        if os.path.exists(savefile):
            with open(savefile,'r') as f:
                self.ip_lst = json.load(f)
            return

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                                   Chrome/83.0.4103.116 Safari/537.36'
        }
        for num in range(1, 60):
            url = 'https://www.kuaidaili.com/free/inha/%d/' % num
            res = requests.get(url, headers=headers, timeout=5)
            html = etree.HTML(res.text)
            ips = html.xpath('//*[@id="list"]/table//tr/td[1]/text()')
            ports = html.xpath('//*[@id="list"]/table//tr/td[2]/text()')
            [self.ip_lst.append('%s:%s' % (ip, port)) for ip, port in zip(ips, ports)]
            time.sleep(2)
            print('IP获取成功，数量%d' % len(self.ip_lst))

        with open(savefile,'w') as sf:
            json.dump(self.ip_lst,sf,ensure_ascii=False)

    '''根据url，请求html'''
    def get_html(self, url, charts = 'gbk'):

        url = self.url_traceback(url)

        at = 2 + 3 * random.random()
        print('sleep...%s'%at)
        time.sleep(at)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        html = ''
        try:
            res = requests.get(url, headers=headers, timeout=10)
            res.encoding = charts
            html = res.text
        except:
            print('error:1',url)
            try:
                req = urllib.request.Request(url=url, headers=headers)
                res = urllib.request.urlopen(req, timeout=10)
                html = res.read().replace(b'\xe5\xbc\x80\xe5\xa7\x8b',b'').decode(charts)
            except:
                print('error:2')
                try:
                    headers = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'br, gzip, deflate',
                        'Accept-Language': 'zh-cn',
                        'Connection': 'keep-alive',
                        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
                        # 'User-Agent': self.ua.random,
                        'User-Agent': random.choice(self.user_agent)
                    }
                    proxy = {'http': random.choice(self.ip_lst)}
                    res = requests.get(url, proxies=proxy, allow_redirects=True,timeout=10)
                    res.encoding = charts
                    html = res.text
                except:
                    print('error:3')
                    try:
                        headers = {
                            'Accept': '*/*',
                            'Accept-Encoding': 'br, gzip, deflate',
                            'Accept-Language': 'zh-cn',
                            'Connection': 'keep-alive',
                            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
                            # 'User-Agent': self.ua.random,
                            'User-Agent': random.choice(self.user_agent)
                        }
                        proxy = {'http': random.choice(self.ip_lst)}
                        proxy_handler = urllib.request.ProxyHandler(proxy)
                        opener = urllib.request.build_opener(proxy_handler)
                        req = urllib.request.Request(url=url, headers=headers)
                        res = opener.open(req, timeout=10)

                        html = res.read().replace(b'\xe5\xbc\x80\xe5\xa7\x8b', b'').decode(charts)
                    except:
                        print('error:4')
                        pass
        return html

    '''根据url，代理，请求html'''
    def get_html_proxy(self, url, charts = 'gbk'):
        url = self.url_traceback(url)
        # headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #            'Host': 'jib.xywy.com',
        #            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
        #            'Accept-Language': 'zh-cn',
        #            'Accept-Encoding': 'gzip, deflate',
        #            'Connection': 'keep-alive'
        # }

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-cn',
            'Connection': 'keep-alive',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
            # 'User-Agent': self.ua.random,
            'User-Agent': random.choice(self.user_agent)
        }

        ips = random.choice(self.ip_lst)
        # proxy = {'http': ips,'https': ips}
        proxy = {'http': ips}
        # proxy = {}

        res = requests.get(url, proxies=proxy,allow_redirects=True)
        print(res.text)

        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        req = urllib.request.Request(url=url, headers=headers)
        res = opener.open(req,)

        html = res.read().replace(b'\xe5\xbc\x80\xe5\xa7\x8b',b'').decode(charts)
        return html

    def get_html2(self, url):
        url = self.url_traceback(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        res = requests.get(url, headers=headers, timeout=20)
        html = res.text
        return html

    def url_traceback(self, url):
        '''路径回溯处理'''
        if '..' not in url:
            return url

        data = url.split('/')
        new_data = []
        for p in data:
            if p=='..':
                new_data.pop(-1)
            else:
                new_data.append(p)

        new_url = '/'.join(new_data)

        return new_url

    def save_image(self, image_url, name, path='./'):

        savefile = os.path.join(path, name+'.jpg')
        if os.path.exists(savefile):
            return
        r = requests.get(image_url)
        with open(savefile,'wb') as sf:
            sf.write(r.content)

    def _getStartEndday(self, start_date,end_date):
        # date = '20191216'
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

        # today = datetime.date.today()
        n = (end_date - start_date).days

        somedays = [datetime.timedelta(days=i) for i in range(n, 0, -1)]
        dates = [datetime.datetime.strftime(end_date - oneday, "%Y-%m-%d") for oneday in somedays]
        return dates
