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
    '''
    url='https://www.zhihu.com/people/excited-vczh/answers'
    '''
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse)



    def parse_follows(self, response):
        pass


    def parse_followers(self, response):
        pass