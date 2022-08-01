#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     selenium.py
# author:   zlw2008ok@126.com
# date:     2022/4/30
# description:    
#
# cmd>e.g.:  
# *****************************************************


"""
selenium爬虫主要是模拟人的点击操作
selenium驱动浏览器并进行操作的过程是可以观察到的
就类似于你在看着别人在帮你操纵你的电脑，类似于别人远程使用你的电脑
当然了，selenium也有无界面模式
https://blog.csdn.net/weixin_43881394/article/details/108827233
"""

"视频示例：" \
"https://www.ixigua.com/7010626084026712590?wid_try=1"

from selenium import webdriver
from time import sleep
import datetime


# 打开浏览器
driver = webdriver.Chrome("./chromedriver")  # 需要下载浏览器对应版本，https://chromedriver.chromium.org/downloads

# 打开网站
url = 'https://www.taobao.com/'
driver.get(url)

# 点击某按钮，弹出登陆页面
if driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul/li[7]/a[1]'):
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul/li[7]/a[1]').click()  # 获取xpath, 浏览器开发模式点击模式copy-->xpath

# 给个时间，手动扫码
sleep(10)

# 进入购物车
car_url = 'https://car.taobao.com/cart.htm'
driver.get(car_url)

# 购买
buytime = '2022-02-01 23:59:59'
while True:
    # 等待抢购时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if now > buytime:
        while True:
            try:
                # 全选购物车
                if driver.find_element_by_xpath(""):
                    pass
            except:
                pass





