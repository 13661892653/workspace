#coding=utf-8
'''
Tools:PyCharm 2017.1
Py:Python3.5
Author:colby_chen
Date:2017-04-13
'''
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from novel.items import NovelItem
class novSpider(CrawlSpider):
    name="novelspider"
    redis_key="novelspider:start_urls"
    start_urls=['http://www.daomubiji.com']
    def parse(self,response):
        #print('response',response)
        selector=Selector(response)
        #print('selector',selector.extract())
        #table=selector.xpath('//table')
        article = selector.xpath('//*[@class="article-content"]//a')
        print('xxxxxxxxxxxxxxxxxxtable',article)
        print('xxxxxxxxxxxxxxxxxxtable',article.extract())
        for each in article:
            print('each',each)
            bookName=each.xpath('a/div/h2/text()').extract()
            print('bookName',bookName)
            content=each.xpath('a/div/p/text()').extract()
            print('content',content)
            url=each.xpath('a/@href').extract()
            print('url',url)
            for i in range(len(url)):
                print('i',i)
                item=NovelItem()
                item['bookName']=bookName
                item['chapterURL']=url[i]
                '''try:
                    item['bookTitle']=content[i].split(' ')[0]
                    item['chapterNum'] = content[i].split(' ')[1]
                except Exception as e:
                    continue
                try:
                    item['chapterName'] = content[i].split(' ')[2]
                except Exception as e:
                    item['chapterName'] = content[i].split(' ')[1][-3:]'''
                print('item',item)
                yield item

