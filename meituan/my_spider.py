#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     my_02.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-06-04
# brief:    
#
# cmd>e.g:  
# *****************************************************

import json
import math
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from lxml import etree
from fake_useragent import UserAgent


class MeituanSpider():

    def __init__(self):
        self.count = 0
        self.ip_lst = []
        self.user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
                         'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
                         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
                         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',


                         ]  #
        self.ua = UserAgent(verify_ssl=False)  # 通过库随机产生useragent
        self.ua.update()
        # self.user_agent = self.ua.get_useragent_list()

    def get_ip(self,savefile):
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

    # 获取页面数据，将json object转化为python dict
    def _get_url(self, url, city):
        simulateBrowserData = {
            'Accept': '*/*',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-cn',
            'Connection': 'keep-alive',
            'Host': city + '.meituan.com',
            'Referer': 'https://' + city + '.meituan.com/meishi/',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
            'User-Agent': self.ua.random,
            # 'User-Agent': random.choice(self.user_agent)

        }

        proxy = {'http': random.choice(self.ip_lst)}
        response = requests.get(url, headers=simulateBrowserData,proxies=proxy, allow_redirects=False)

        soup = BeautifulSoup(response.text)
        # for script in soup.find_all('script'):
        #    print(script.contents)
        all_scripts = soup.find_all('script')
        text = None
        for number, script in enumerate(all_scripts):
            if 'window._appState' in script.text:
                text = script.text
                # print(number, text)
        if text == None:
            print("服务器拒绝访问")
            # print(simulateBrowserData['User-Agent'])
            time.sleep(1+2*random.random())
            self.count += 1
            if self.count>6:
                print('sleep 600s...')
                time.sleep(600)  # 连续失败n次，休息10分钟再请求
                self.count=0
            return self._get_url(url,city)  # user-agent 失效情况 继续随机一个进行请求
        else:
            self.count = 0
            data = json.loads(text.split("=", 1)[1][:-1])
            print(simulateBrowserData['User-Agent'])
            return data

    # 获取店铺评论数据
    def _get_comment(self, ):
        '''https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=763c7334407e4fb1aef8.1622721180.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F913072238%2F&riskLevel=1&optimusCode=10&id=913072238&userId=147136762&offset=0&pageSize=10&sortType=1'''

    # 获取一个城市多区域多类目商家信息
    def get_city_shops_infos(self,city, categoryID, sf):
        '''美团商家信息最大显示67页，所以应该按各个小分类进行爬取，尽量列出所有店铺'''

        if not self.ip_lst:
            with open('ips.json','r') as f:
                self.ip_lst = json.load(f)
        success_shops = set()
        failed_shops = set()
        # city = 'bj'
        url = 'https://' + city + '.meituan.com/meishi/' + categoryID + '/'

        data = self._get_url(url, city)
        n = 0

        filters = data.get('filters',{})

        cates = filters.get('cates',[])  # 分类
        areas = filters.get('areas',[])  # 区域
        dinners = filters.get('dinnerCountsAttr',[])  # 用餐人数
        sorts = filters.get('sortTypesAttr',[])  # 店铺排序类型

        # 这里只考虑'区域'
        for _area in areas[:]:
            '''一级：大区域'''
            area_id = _area['id']  # int
            area_name = _area['name']
            print('大区域：', area_name)

            area_url = _area['url']
            sub_areas = _area.get('subAreas',[])
            if not sub_areas:continue

            for _sub_area in sub_areas[1:]:  # 第一个元素为大区域"全部"
                '''二级：小区域'''
                sub_area_id = _sub_area['id']  # int
                sub_area_name = _sub_area['name']
                print('小区域：', sub_area_name)

                sub_area_url = _sub_area['url'].replace('http:','https:')
                print(sub_area_url)
                a_data = self._get_url(sub_area_url, city)

                shopCounts = a_data.get('poiLists').get('totalCounts')  # 最小区域内的商家数量
                pageNum = math.ceil(shopCounts / 15)  # 美团一页展示15个商家

                for pn in range(1,pageNum+1):
                    print('page:', pn)
                    try:
                        for eachShopInfo in a_data.get('poiLists').get('poiInfos'):
                            shopId = eachShopInfo.get('poiId')  # 店铺id
                            try:
                                if shopId in success_shops:continue

                                n += 1
                                # if n < 1215:  # todo: 中断跳过操作
                                #     print('===== 跳过 =====')
                                #     continue
                                print(n)

                                shopName = eachShopInfo.get('title')  # 店铺名
                                print(shopName)
                                avgScore = eachShopInfo.get('avgScore')  # 评分
                                allCommentNum = eachShopInfo.get('allCommentNum')  # 评论条数
                                address = eachShopInfo.get('address')  # 地址
                                avgPrice = eachShopInfo.get('avgPrice')  # 人均价格

                                # 店铺详细信息
                                shop_url = 'https://www.meituan.com/meishi/%s/' % shopId
                                print(shop_url)
                                shop_data = self._get_url(shop_url,'nc')
                                recommended = shop_data.get('recommended',[])  # 推荐菜
                                shopClass = [_d['title'] for _d in shop_data.get('crumbNav',[])]  # 店铺层级
                                phone = shop_data.get('detailInfo',{}).get('phone','')  # 电话
                                address_detail = shop_data.get('detailInfo', {}).get('address', '')  # 详细地址
                                openTime = shop_data.get('detailInfo',{}).get('openTime','')  # 营业时间
                                dealList = shop_data.get('dealList',{}).get('deals',[])  # 套餐列表

                                success_shops.add(shopId)

                                out_data = [city,categoryID,area_name,sub_area_name,shopId,shopName,avgScore,allCommentNum,avgPrice,address_detail,'/'.join(shopClass),
                                            phone,openTime,shop_url,json.dumps(recommended,ensure_ascii=False),json.dumps(dealList,ensure_ascii=False)]

                                out_data = [str(_str).replace('\t','|') for _str in out_data]
                                out_str = '\t'.join(out_data)
                                sf.write(out_str+'\n') if sf else print(out_str)

                                time.sleep(20+ 5*random.random())
                            except Exception as e:
                                print("error:%s" % e)
                                print("shopId:%s" % shopId)
                                time.sleep(1+6*random.random())
                    except Exception as e:
                        print("error:%s" % e)
                        print("page:%s" % pn)
                        time.sleep(1 + 6 * random.random())



                    pn += 1
                    next_page_url = sub_area_url+'pn%s/' % pn
                    if pn > pageNum:break
                    a_data = self._get_url(next_page_url, city)







if __name__=="__main__":
    mt = MeituanSpider()
    # mt.get_ip('ips.json')
    # sf = open('nanchang_xc_shops.txt','w')  # xc:c35
    sf = open('nanchang_dgtd_shops.txt', 'w')  # dgtd:c11
    data = mt.get_city_shops_infos('nc','c11',sf)
    sf.close()


