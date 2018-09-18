# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlrd, xlwt

class ScrapysPipeline(object):
    def process_item(self, item, spider):
        return item

class LianJiaPipeline(object):
    def __init__(self):
        self.filename = 'results/tianjing_houses.xls'
        self.outputbook = xlwt.Workbook()
        self.table = self.outputbook.add_sheet('sheet1', cell_overwrite_ok=True)
        self.nrow = 0

    def process_item(self, item, spider):
        self.table.write(self.nrow, 0, item['name'])
        self.table.write(self.nrow, 1, item['type'])
        self.table.write(self.nrow, 2, ' '.join(item['area_range']))
        self.table.write(self.nrow, 3, item['mean_price'])
        self.table.write(self.nrow, 4, ' '.join(item['start_price']))
        self.table.write(self.nrow, 5, ' '.join(item['tags']))

        self.nrow += 1

    def close_spider(self, spider):
        self.outputbook.save(self.filename)
