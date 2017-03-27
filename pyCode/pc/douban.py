#coding=utf-8
from scrapy.spiders import CrawlSpider
class Douban(CrawlSpider):
	name = "douban"
	start_urls = ['http://movie.douban.com/top250']
	def parse(self,response):
		print (response.body)
if __name__=='__main__':
    spd=Douban()
    spd.parse('dddddd')