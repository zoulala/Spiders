#coding=utf8
import re
import scrapy
from scrapys.items import LianjiaItem
from scrapy.http import Request

class TlsqSpider(scrapy.Spider):
    name = "tlcg"
    # allowed_domains = ["bbs.tl.changyou.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    allowed_domains = ["www.pinduoduo.com"]  # 可选项
    start_urls = [
        "https://www.pinduoduo.com/category/food.html?utm_source=baidubz&utm_medium=BrandZ&utm_term=&utm_campaign=search&utm_content=logolink"
        # "http://bbs.tl.changyou.com/forum.php?mod=forumdisplay&fid=510"
    ]

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个Request请求
        :return:
        """
        # 请求self.start_urls[0],返回的response会被送到回调函数parse中
        yield Request(self.start_urls[0])

    def parse(self, response):
        page_max = int(re.findall(u'\u5171(.*?)\u9875', response.body.decode('utf8'))[0] ) # get max num of pages
        for i in range(4001, 8000+1): #1-1000,1001-2000,...,7001-8000
            next_url = response.url + '&page=' + str(i)
            yield Request(next_url, callback=self.sub1_parse)


    def sub1_parse(self, response):
        ulr_list = response.xpath('//a[@class="s xst"]/@href').extract()  # extract将xpath对象转换为Unicode字符串列表。get urls from a page
        for url in ulr_list:
            url = "http://bbs.tl.changyou.com/" + url
            yield Request(url, callback=self.sub2_parse)

    def sub2_parse(self, response):
        page_r = re.findall(u'\u5171(.*?)\u9875', response.body.decode('utf8'))  # get max num of pages
        if page_r == []:
            page_max = 1
        else:
            page_max = int(page_r[0])
        print ('------------------', page_max)
        for i in range(1, page_max+1):
            next_url = response.url + '&page=' + str(i)
            try:
                yield Request(next_url, callback=self.sub3_parse)
            except:
                continue

    def sub3_parse(self, response):
        item = TianlongItem()
        text_list = response.xpath('//td[@class="t_f"]/text()').extract()  # get contents of a url
        item['content'] = ''.join(text_list)
        print ('=====================output')
        yield item
