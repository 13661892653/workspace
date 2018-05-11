# -*- coding: utf-8 -*-
import scrapy
from quotetutorial.items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    #parse 默认回调函数
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item=QuotetutorialItem()
            #extract_first 返回单个结果，extract返回一个列表
            text   = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags   = quote.css('.tags .tag::text').extract()
            item['text']= text
            item['author'] = author
            item['tags'] = tags
            yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        print("下一页URL地址：",next)
        #response.urljoin=start_urls + url
        url=response.urljoin(next)
        print("下一页URL地址：", url)
        yield scrapy.Request(url=url,callback=self.parse)