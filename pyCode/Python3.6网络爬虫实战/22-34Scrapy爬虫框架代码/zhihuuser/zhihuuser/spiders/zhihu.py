# -*- coding: utf-8 -*-
'''
scrapy startproject zhihuuser
scrapy genspider zhihu www.zhihu.com
'''
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
