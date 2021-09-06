#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     xmly_spider.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-08-07
# brief:    
#
# cmd>e.g:  
# *****************************************************

import requests
import os
import time
import execjs
import hashlib
import random




'''爬取喜马拉雅服务器系统时间戳，用于生成xm-sign'''
def getxmtime():
    url="https://www.ximalaya.com/revision/time"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+ xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q=0.8, application/signe-exchange;v = b3',
        'Host': 'www.ximalaya.com'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html

'''利用xmSign.js生成xm-sign'''
def exec_js():
    #获取喜马拉雅系统时间戳
    time = getxmtime()

    #读取同一路径下的js文件
    with open('xmSign.js',"r",encoding='utf-8') as f:
        js = f.read()

    # 通过compile命令转成一个js对象
    docjs = execjs.compile(js)
    # 调用js的function生成sign
    res = docjs.call('python',time)
    return res

def getSign(): # 加密值
    """
    生成 xm-sign
    规则是 md5(himalaya-服务器时间戳)(100以内随机数)服务器时间戳(100以内随机数)现在时间戳
    :return: sign
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+ xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q=0.8, application/signe-exchange;v = b3',
        'Host': 'www.ximalaya.com'
    }
    serverTimeUrl = "https://www.ximalaya.com/revision/time"
    # 获取服务器时间
    serverTime = requests.get(serverTimeUrl, headers=headers).text
    nowTime = str(round(time.time()*1000))
    sign = str(hashlib.md5("himalaya-{}".format(serverTime).encode()).hexdigest()) + "({})".format(str(round(random.random()*100))) + serverTime + "({})".format(str(round(random.random()*100))) + nowTime
    # 将xm-sign添加到请求头中
    return sign


def get_response(html_url):
    at = 3 + random.random() * 3
    print('sleep 1',at)
    time.sleep(at)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=header)
    return response

def get_response2(html_url):
    at = 3 + random.random() * 3
    print('sleep 2',at)
    time.sleep(at)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+ xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q=0.8, application/signe-exchange;v = b3',
        'Host': 'www.ximalaya.com'
    }
    # xm_sign = exec_js()
    xm_sign = getSign()
    # 将生成的xm-sign添加到请求投中
    headers["xm-sign"] = xm_sign
    response = requests.get(url=html_url, headers=headers)

    return response


def save(name, title, audio_url):
    path = f'data/{name}/'
    if not os.path.exists(path):
        os.makedirs(path)
    audio_content = get_response(audio_url).content
    with open(path + title + '.m4a', mode='wb') as f:
        print(path+title)
        f.write(audio_content)
        print('已保存：', title)
    with open(path + title + '.txt', mode='w') as sf:
        sf.write(audio_url)


def get_audio_url(audio_id):
    page_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={audio_id}&ptype=1'
    # print(page_url)
    try:
        json_data = get_response2(page_url).json()
    except:
        json_data = get_response2(page_url).json()
    audio_url = json_data['data']['src']
    print(audio_url)
    return audio_url


def get_audio_info(html_url, book):
    json_data = get_response(html_url).json()
    audio_info = json_data['data']['tracks']
    for index in audio_info:
        try:
            # 音频ID
            audio_id = index['trackId']
            # 章节名字
            audio_title = index['title']
            # 有声书小说名字 《摸金天师》第001章 百辟刀
            # audio_name = audio_title.split('第')[0]
            audio_url = get_audio_url(audio_id)
            save(book, audio_title, audio_url)
        except Exception as e:
            print('error:%s' % e)


if __name__ == '__main__':
    sources = {'3179882':'环球人物',
               '11183267':'世界顶级思维',
               '3580611':'李嘉诚：成功没有偶然',
               '8214178':'马云正传',
               '23886769':'马化腾传',
               '34362217':'稻盛和夫',
               '3705693':'股票投资教学',
               }

    for _id in sources:
        book = sources[_id]

        for page in range(1, 39):
            print('page:',page)
            url = f'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={_id}&pageNum={page}'
            # book = '世界顶级思维'
            try:
                get_audio_info(url, book)
            except:
                get_audio_info(url, book)