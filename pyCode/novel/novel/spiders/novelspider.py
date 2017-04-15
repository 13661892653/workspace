#coding=utf-8
'''
Tools:PyCharm 2017.1
Py:Python3.5
Author:colby_chen
Date:2017-04-13
'''
from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector, HtmlXPathSelector
from novel.items import NovelItem
class novSpider(CrawlSpider):
    name="novelspider"
    redis_key="novelspider:start_urls"
    start_urls=['http://www.daomubiji.com']

    def parse_item(self, response):
        sell = Selector(response)
        sites = sell.xpath('/html/body/section/div[2]/div/article/a/text()').extract()
        print('sites',sites)
        item={}
        for site in sites:
            print(site)
            item['zj']=site
            print(item)
            yield item
    def parse(self,response):
        #print('response',response)
        selector=Selector(response)
        #print('selector',selector.extract())
        #table=selector.xpath('//table')
        article = selector.xpath('//article/p/a')
        #print('xxxxxxxxxxxxxxxxxxtable',article)
        #print('xxxxxxxxxxxxxxxxxxtable',article.extract())
        items=[]
        for each in article:
            #print('each',each)
            url = each.xpath('@href').extract()[0]
            items.append(url)
        print(items)
        for item in items:
            yield Request(item, callback=self.parse_item)
            #bookName=each.xpath('div/h2/text()').extract()
            #print('bookName',bookName)
            #content=each.xpath('div/p/text()').extract()
            #print('content',content)

        '''
        print('url',url)
        for i in range(len(url)):
            print('i',i)
            item=NovelItem()
            item['bookName']=bookName
            item['chapterURL']=url[i]
            print('item',item)
            #yield item
        '''