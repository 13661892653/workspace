# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org/']
    start_urls = ['http://httpbin.org/post']

    def start_requests(self):
        #POST方式提交请求
        yield scrapy.Request(url=self.start_urls[0],method='POST',callback=self.parse_post)

    def parse(self, response):
        pass

    def parse_post(self,response):
        print(response.status)