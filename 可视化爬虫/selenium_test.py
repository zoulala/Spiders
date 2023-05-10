#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     test.py
# author:   zlw2008ok@126.com
# date:     2023/2/16
# desc:     
#
# cmd>e.g.:  
# *****************************************************
from bs4 import BeautifulSoup
from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver import ActionChains  # 破解滑动验证码的时候用的 可以拖动图片
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
# ref:https://www.cnblogs.com/lweiser/p/11045023.html

# 打开浏览器
driver = webdriver.Chrome("./chromedriver")  # 需要下载浏览器对应版本，https://chromedriver.chromium.org/downloads

# 访问页面
driver.get('https://item.jd.com/13652780.html')

# 获取页面源码
html = driver.page_source

# 创建Beautifulsoup对象
soup = BeautifulSoup(html, 'html.paser')

# 查找用户评论内容
comments = soup.find_all('div',{'class':'comment-text'})

# 输出评论
results = [comment.get_text() for comment in comments]
print(results)

# 关闭浏览器
driver.quit()
