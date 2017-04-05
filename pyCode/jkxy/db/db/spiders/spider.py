#coding=utf-8
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
from scrapy.spiders import CrawlSpider
class db(CrawlSpider):
    name="doubanTest"
    start_urls=['http://movie.douban.com/top250']
    def parse(self,response):
        print(response.body)
        print(response.url)