#coding=utf8
import re

import scrapy
from scrapy.http import Request

from scrapys.items import LianjiaItem


# scrapy用yield异步处理网页，想顺序处理网页，可以参考https://stackoverflow.com/questions/6566322/scrapy-crawl-urls-in-order

class LJ_houseSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["gz.fang.lianjia.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        "http://gz.fang.lianjia.com/loupan/"
    ]

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个Request请求
        :return:
        """
        # 请求self.start_urls[0],返回的response会被送到回调函数parse中
        yield Request(self.start_urls[0])

    def parse(self, response):

        max_page_text = response.xpath('//div[@class="page-box"]/@data-total-count').extract()
        nums = re.findall(r'(\d+)',max_page_text[0])
        max_num = int(nums[0])
        max_num //= 10
        print('max page>>>>>>>>>>>',max_num)
        for i in range(max_num):
            print(i)
            url = self.start_urls[0]+'pg'+str(i+1)
            yield Request(url, callback=self.extract_content, priority=max_num-i)  #该方法及其他的Request回调函数必须返回一个包含 Request 及(或) Item 的可迭代的对象

        

    def extract_content(self, response):
        paths = response.xpath('//ul[@class="resblock-list-wrapper"]/li')
        items = []
        for sel in paths:
            item = LianjiaItem()
            name = sel.xpath('div/div[@class="resblock-name"]/a[@class="name"]/text()').extract()
            type = sel.xpath('div/div[@class="resblock-name"]/span[@class="resblock-type"]/text()').extract()
            area_range = sel.xpath('div/div[@class="resblock-area"]/span/text()').extract()
            mean_price = sel.xpath('div/div[@class="resblock-price"]/div[@class="main-price"]/span[@class="number"]/text()').extract()
            mean_unit = sel.xpath('div/div[@class="resblock-price"]/div[@class="main-price"]/span[@class="desc"]/text()').extract()
            start_price = sel.xpath('div/div[@class="resblock-price"]/div[@class="second"]/text()').extract()
            tags = sel.xpath('div/div[@class="resblock-tag"]/span/text()').extract()

            item['name'] = name[0] if name else 'NAN'
            item['type'] = type[0] if type else 'NAN'
            item['area_range'] = re.findall(r'\d+',area_range[0])+re.findall(r'-[\d+](.)+',area_range[0]) if area_range else []
            item['mean_price'] = mean_price[0] +' '+ ' '.join(re.findall(r'\w[/]\w',mean_unit[0])) if mean_price and mean_unit else 'NAN'
            item['start_price'] = re.findall(r'\d+',start_price[0])+re.findall(r'[\d+](.)+[/]',start_price[0]) if start_price else []
            item['tags'] = tags
            items.append(item)
        return items