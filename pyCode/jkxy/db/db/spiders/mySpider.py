#coding=utf-8
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from db.items import *
'''爬取准备
*目标网站：豆瓣电影TOP250
*目标网址：http://movie.douban.com/top250
*目标内容：
    *豆瓣电影TOP250部电影的以下信息
    *电影名称
    *电影信息
    *电影评分
*输出结果：生成csv文件
'''
class Douban(CrawlSpider):
    name = "doubanMovie"
    redis_key='douban:start_urls'
    start_urls=['http://movie.douban.com/top250']
    url='http://movie.douban.com/top250'
    def parse(self,response):
        item=DbItem()
        selector=Selector(response)
        Movies=selector.xpath('//div[@class="info"]')
        for eachMoive in Movies:
            title=eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle=''
            for each in title:
                fullTitle+=each
            movieInfo=eachMoive.xpath('div[@class="bd"]/p/text()').extract()
            star=eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
            quote=eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote=quote[0]
            else:
                quote=''
            item['title']=fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
        nextLink=selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink=nextLink[0]
            print(nextLink)
            yield Request(self.url+nextLink,callback=self.parse)

