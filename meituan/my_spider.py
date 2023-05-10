#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     my_02.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-06-04
# brief:    pc端base_url = https://nc.meituan.com/meishi/  ； h5端base_url = http://meishi.meituan.com/i/?cateId=35&onlylist=1
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

'''
ref1: https://www.futaike.net/archives/6834.html

'''


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
        self.ua = UserAgent()  # 通过库随机产生useragent
        self.ua.update()
        # self.user_agent = self.ua.get_useragent_list()
        self.areas_id = []  # 区域id

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
            print('page %s IP获取成功，数量%d' % (num, len(self.ip_lst)))

        with open(savefile,'w') as sf:
            json.dump(self.ip_lst,sf,ensure_ascii=False)

    def load_ids(self, city='nc',savefile='areas.json'):
        '''加载城市下所有区域id'''
        savefile = city+'_'+savefile

        if os.path.exists(savefile):
            self.areas_id = json.load(open(savefile, 'r'), )
            if not self.areas_id:  # 文件空时，重新获取ids
                self.areas_id, _ = self._get_all_areas_ids(city)
                with open(savefile, 'w') as sf:
                    json.dump(self.areas_id, sf, ensure_ascii=False)

        else:
            self.areas_id, _ = self._get_all_areas_ids(city)
            with open(savefile,'w') as sf:
                json.dump(self.areas_id,sf,ensure_ascii=False)


    # 获取页面数据，将json object转化为python dict
    def _get_url(self, url, city):
        time.sleep(6+10*random.random())
        simulateBrowserData = {
            # 'Accept': '*/*',
            # 'Accept-Encoding': 'br, gzip, deflate',
            # 'Accept-Language': 'zh-cn',
            # 'Connection': 'keep-alive',
            # 'Host': city + '.meituan.com',
            # 'Referer': 'https://' + city + '.meituan.com/meishi/',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
            # 'User-Agent': self.ua.random,
            # 'User-Agent': random.choice(self.user_agent)
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

        }
        simulateBrowserData = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                # 'Cookie':'uuid=ff3f85612b5b4adbbb18.1671341574.1.0.0; _lxsdk_cuid=18523b88c4cc8-065d1500156856-1a535634-fa000-18523b88c4cc8; userTicket=kqtIgajTJgokWUJMzWacBLrIjbhbVkpKsZhvOYnC; u=147136762; n=zou%E5%95%A6%E5%95%A6; m=zlw2008ok%40126.com; lt=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; mt_c_token=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; token=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; token2=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; _lxsdk=18523b88c4cc8-065d1500156856-1a535634-fa000-18523b88c4cc8; unc=zou%E5%95%A6%E5%95%A6; __mta=47044248.1671342138079.1671342138079.1671342138079.1; WEBDFPID=zxw12w4z384u5z6v04y15967v4u193w7812x920u1uv9795876754ux4-1997921431823-1682561431335QEAAEQG75613c134b6a252faa6802015be905511978; ci=1; client-id=51feb11c-0fc7-4401-87bd-2dc36c4a2fb0; firstTime=1683360482003; _lxsdk_s=187f01a757e-d17-93b-8e7%7C%7C2',
                # 'Cookie':'uuid=ff3f85612b5b4adbbb18.1671341574.1.0.0; _lxsdk_cuid=18523b88c4cc8-065d1500156856-1a535634-fa000-18523b88c4cc8; userTicket=kqtIgajTJgokWUJMzWacBLrIjbhbVkpKsZhvOYnC; u=147136762; n=zou%E5%95%A6%E5%95%A6; m=zlw2008ok%40126.com; lt=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; mt_c_token=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; token=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; token2=AgFBIaTOwG_TWpGQr1G27rzzxqv0A4066nPq5lOSi8HDSPsCiWynXdx31GbmdRzxe9gX_VZMQhEgaQAAAACfFQAAWVN7LOoKMChhIu2ZIXG8ipDeLhrOI1rGMOK6JHTmnONpQ4xTb0-zmU2tDIPu02lW; _lxsdk=18523b88c4cc8-065d1500156856-1a535634-fa000-18523b88c4cc8; unc=zou%E5%95%A6%E5%95%A6; __mta=47044248.1671342138079.1671342138079.1671342138079.1; WEBDFPID=zxw12w4z384u5z6v04y15967v4u193w7812x920u1uv9795876754ux4-1997921431823-1682561431335QEAAEQG75613c134b6a252faa6802015be905511978; ci=1; client-id=51feb11c-0fc7-4401-87bd-2dc36c4a2fb0; firstTime=1683362871838; _hc.v=900862a5-59b9-785f-f44f-6d5763451aaf.1683362872; lat=28.700318; lng=115.868838; _lxsdk_s=187f037f9e2-685-364-ec2%7C%7C7',
                # 'Cookie': 'uuid=ff3f85612b5b4adbbb18.1671341574.1.0.0; _lxsdk_cuid=18523b88c4cc8-065d1500156856-1a535634-fa000-18523b88c4cc8; m=zlw2008ok%40126.com; WEBDFPID=zxw12w4z384u5z6v04y15967v4u193w7812x920u1uv9795876754ux4-1997921431823-1682561431335QEAAEQG75613c134b6a252faa6802015be905511978; client-id=51feb11c-0fc7-4401-87bd-2dc36c4a2fb0; _hc.v=900862a5-59b9-785f-f44f-6d5763451aaf.1683362872; lat=28.700318; lng=115.868838; ci=83; rvct=83; __mta=47044248.1671342138079.1671342138079.1683507466981.2; mtcdn=K; IJSESSIONID=node01lr7wyjc0q690q9mmrehr4dx050665205; iuuid=0E42E134BE46138209AC6A4C37D41EDDE41622CCD784D66B36FA1358A6774904; cityname=%E5%8D%97%E6%98%8C; _lxsdk=0E42E134BE46138209AC6A4C37D41EDDE41622CCD784D66B36FA1358A6774904; userTicket=GvDDDSoidEwoVHUPtuTAGYNxyiVjolmBEjUSxUwV; _yoda_verify_resp=ZsJuyiH1rkbRGOD8m%2F2I%2BZiq0qV1Z3DuFrOlkNneHhgGftk17%2B8oEzY95XYglRt9tLcs5Tpm1D7H72DuZUOzPQzrkT1X5ayz1fSlDnJDm4VWKsTJHEJ%2Bg%2BF4qnWU5gzsCOfO%2B4JNWYmaiz7RXqCoRcohu0X6RVlFzOly3s1TdZ3FWPMc8c9Y%2F86zhof4XNSYHutkL3rrJ8XTZ%2FYwpYEedR0Ekf1WgMNZx4tqgdoe08igayLjUZhPLke%2F37z7TJFCjE9DwS8Cy28jMQ7Gm1Wt98aEbrGj66vbViP7fBJEeBQmLxUG3h2WSPBDRC5pqwJW6c7Ymwjka4VKVt7lhDeSUVf4qyMZwUkenZGw9rY98EgpX1NRkiAles4nnwbBk0bX; _yoda_verify_rid=16f9518e66800045; u=147136762; n=zou%E5%95%A6%E5%95%A6; lt=AgEBI4YwWiBnjn7bg-wTaQpiYfc5onCcvl5KmucmBrQVv-duXQLs9TUw5MeasotWSlMx-NgvmMwyAgAAAAAtGAAAR_A9pQ60VqP7Zihos_oXxsxKtAa_VlGkvnP8E7RtXF0w8HZb1shW-0JzxAESgPIX; mt_c_token=AgEBI4YwWiBnjn7bg-wTaQpiYfc5onCcvl5KmucmBrQVv-duXQLs9TUw5MeasotWSlMx-NgvmMwyAgAAAAAtGAAAR_A9pQ60VqP7Zihos_oXxsxKtAa_VlGkvnP8E7RtXF0w8HZb1shW-0JzxAESgPIX; token=AgEBI4YwWiBnjn7bg-wTaQpiYfc5onCcvl5KmucmBrQVv-duXQLs9TUw5MeasotWSlMx-NgvmMwyAgAAAAAtGAAAR_A9pQ60VqP7Zihos_oXxsxKtAa_VlGkvnP8E7RtXF0w8HZb1shW-0JzxAESgPIX; token2=AgEBI4YwWiBnjn7bg-wTaQpiYfc5onCcvl5KmucmBrQVv-duXQLs9TUw5MeasotWSlMx-NgvmMwyAgAAAAAtGAAAR_A9pQ60VqP7Zihos_oXxsxKtAa_VlGkvnP8E7RtXF0w8HZb1shW-0JzxAESgPIX; firstTime=1683523588636; unc=zou%E5%95%A6%E5%95%A6; _lxsdk_s=187f9d23e3d-2e6-aee-0ef%7C%7C13'
                'Cookie': 'uuid=ff3f85612b5b4adbbb18.1671341574.1.0.0; _lxsdk_cuid=18523b88c4cc8-065d1500156856-1a535634-fa000-18523b88c4cc8; m=zlw2008ok%40126.com; WEBDFPID=zxw12w4z384u5z6v04y15967v4u193w7812x920u1uv9795876754ux4-1997921431823-1682561431335QEAAEQG75613c134b6a252faa6802015be905511978; client-id=51feb11c-0fc7-4401-87bd-2dc36c4a2fb0; _hc.v=900862a5-59b9-785f-f44f-6d5763451aaf.1683362872; lat=28.700318; lng=115.868838; ci=83; rvct=83; mtcdn=K; IJSESSIONID=node01lr7wyjc0q690q9mmrehr4dx050665205; iuuid=0E42E134BE46138209AC6A4C37D41EDDE41622CCD784D66B36FA1358A6774904; cityname=%E5%8D%97%E6%98%8C; _lxsdk=0E42E134BE46138209AC6A4C37D41EDDE41622CCD784D66B36FA1358A6774904; userTicket=GvDDDSoidEwoVHUPtuTAGYNxyiVjolmBEjUSxUwV; p_token=AgEBI4YwWiBnjn7bg-wTaQpiYfc5onCcvl5KmucmBrQVv-duXQLs9TUw5MeasotWSlMx-NgvmMwyAgAAAAAtGAAAR_A9pQ60VqP7Zihos_oXxsxKtAa_VlGkvnP8E7RtXF0w8HZb1shW-0JzxAESgPIX; __utma=74597006.486048527.1683530830.1683530830.1683530830.1; __utmc=74597006; __utmz=74597006.1683530830.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=74597006.9.8.1683530853930; qruuid=15b80bc4-d6ad-491f-a390-10e1e0986217; token2=AgEqIAGi4qChebfRbARm2NwNPqTl6hI5CyWHDdndN15WRYw62MQFE97Ea9NpdRlxHsyz_6lhbBdUfAAAAABKGAAAOt8GR3dX9EAYe-KRVtcLBWs7XaHVWE_u_IO6QvIhgtQ3Gb9K7O9JCeckQqE0PAbn; oops=AgEqIAGi4qChebfRbARm2NwNPqTl6hI5CyWHDdndN15WRYw62MQFE97Ea9NpdRlxHsyz_6lhbBdUfAAAAABKGAAAOt8GR3dX9EAYe-KRVtcLBWs7XaHVWE_u_IO6QvIhgtQ3Gb9K7O9JCeckQqE0PAbn; lt=AgEqIAGi4qChebfRbARm2NwNPqTl6hI5CyWHDdndN15WRYw62MQFE97Ea9NpdRlxHsyz_6lhbBdUfAAAAABKGAAAOt8GR3dX9EAYe-KRVtcLBWs7XaHVWE_u_IO6QvIhgtQ3Gb9K7O9JCeckQqE0PAbn; u=147136762; n=zou%E5%95%A6%E5%95%A6; unc=zou%E5%95%A6%E5%95%A6; __mta=47044248.1671342138079.1683530759991.1683530990404.5; firstTime=1683530998804; _lxsdk_s=187fa40b86a-5db-2b0-5d9%7C%7C12'
        }

        proxy = {'http': random.choice(self.ip_lst)}
        response = requests.get(url, headers=simulateBrowserData, proxies=proxy, allow_redirects=False)

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
            time.sleep(5+2*random.random())
            self.count += 1
            if self.count>6:
                print('sleep 600s...')
                self.count = 0
                # time.sleep(600)  # 连续失败n次，休息10分钟再请求
                return {}
            return self._get_url(url,city)  # user-agent 失效情况 继续随机一个进行请求
        else:
            self.count = 0
            data = json.loads(text.split("=", 1)[1][:-1])
            print(simulateBrowserData['User-Agent'])
            return data

    # 获取店铺评论数据
    def _get_comment(self, ):
        '''https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=763c7334407e4fb1aef8.1622721180.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F913072238%2F&riskLevel=1&optimusCode=10&id=913072238&userId=147136762&offset=0&pageSize=10&sortType=1'''

    # 获取城市美食的所有区域和子区域id
    def _get_all_areas_ids(self, city='nc'):
        ids = []
        urls = []
        base_url = 'https://' + city + '.meituan.com/meishi/'
        data = self._get_url(base_url, city)

        filters = data.get('filters', {})
        cates = filters.get('cates', [])  # 分类
        areas = filters.get('areas', [])
        dinners = filters.get('dinnerCountsAttr',[])  # 用餐人数
        sorts = filters.get('sortTypesAttr',[])  # 店铺排序类型

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

                ids.append((area_name,area_id,sub_area_name,sub_area_id))
                urls.append(sub_area_url)
        return ids, urls

    # 获取商铺详细信息
    def _get_shop_infos(self, shopId):
        shop_url = 'https://www.meituan.com/meishi/%s/' % shopId
        print(shop_url)
        shop_data = self._get_url(shop_url, 'nc')
        recommended = shop_data.get('recommended', [])  # 推荐菜
        shopClass = [_d['title'] for _d in shop_data.get('crumbNav', [])]  # 店铺层级
        phone = shop_data.get('detailInfo', {}).get('phone', '')  # 电话
        address_detail = shop_data.get('detailInfo', {}).get('address', '')  # 详细地址
        openTime = shop_data.get('detailInfo', {}).get('openTime', '')  # 营业时间
        dealList = shop_data.get('dealList', {}).get('deals', [])  # 套餐列表

        res = [shop_url,recommended,shopClass,phone,address_detail,openTime,dealList]
        return res

    # 获取一个城市多区域多类目商家信息
    def get_city_shops_infos(self,city, categoryID, sf):
        '''美团商家信息最大显示67页，所以应该按各个小分类进行爬取，尽量列出所有店铺'''

        if not self.ip_lst:
            with open('ips.json','r') as f:
                self.ip_lst = json.load(f)
        success_shops = set()
        failed_shops = set()

        if not self.areas_id:
            self.load_ids(city)

        n = len(self.areas_id)
        print('n:',n)
        for i in range(9,n):
            print(f'------------- {i} -------------')
            area_name,area_id,sub_area_name,sub_area_id = self.areas_id[i]
            print(f'--{area_name} -- {sub_area_name} -- {sub_area_id}--')

            sub_area_url = 'https://' + city + '.meituan.com/meishi/'+ categoryID + 'b'+str(sub_area_id)+'/'

            a_data = self._get_url(sub_area_url, city)

            shopCounts = a_data.get('poiLists').get('totalCounts')  # 最小区域内的商家数量
            pageNum = math.ceil(shopCounts / 15)  # 美团一页展示15个商家

            for pn in range(1,pageNum+1):
                print('page:', pn)
                try:
                    for eachShopInfo in a_data.get('poiLists').get('poiInfos'):
                        # 获取每个店铺数据
                        shopId = eachShopInfo.get('poiId')  # 店铺id

                        try:
                            if shopId in success_shops:continue

                            shopName = eachShopInfo.get('title')  # 店铺名
                            print(shopName)
                            avgScore = eachShopInfo.get('avgScore')  # 评分
                            allCommentNum = eachShopInfo.get('allCommentNum')  # 评论条数
                            address = eachShopInfo.get('address')  # 地址
                            avgPrice = eachShopInfo.get('avgPrice')  # 人均价格

                            # 获取店铺详细信息
                            shop_url,recommended, shopClass, phone, address_detail, openTime, dealList = self._get_shop_infos(shopId)

                            success_shops.add(shopId)
                            out_data = [city,categoryID,area_name,sub_area_name,i,shopId,shopName,avgScore,allCommentNum,avgPrice,address_detail,'/'.join(shopClass),
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


                # 获取下一页
                pn += 1
                next_page_url = sub_area_url+'pn%s/' % pn
                if pn > pageNum:break
                a_data = self._get_url(next_page_url, city)





if __name__=="__main__":
    mt = MeituanSpider()
    # mt.get_ip('ips.json')
    # sf = open('nanchang_xc_shops_0505.txt','w')  # xc:c35
    # data = mt.get_city_shops_infos('nc', 'c35', sf)
    # sf.close()
    sf = open('nanchang_dgtd_shops_0505.txt', 'w')  # dgtd:c11
    data = mt.get_city_shops_infos('nc','c11',sf)
    sf.close()
    print('finished!')


