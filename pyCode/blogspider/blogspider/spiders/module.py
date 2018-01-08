#coding=utf-8
#import scrapy
#from bs4 import BeautifulSoup
import re
from scrapy.spiders import CrawlSpider
from blogspider.items import BlogspiderItem
from scrapy.selector import Selector, HtmlXPathSelector
class Qiye_spider(CrawlSpider):
    name = 'module'
    key = "modele:start_urls"
    start_urls = ['https://www.cnblogs.com/qiyeboy/']
    def parse(self, response):
        pages = re.findall(re.compile(r'<div class="day">([\S\s]*?<a href=)'), response)
        for page in pages:
            url = re.findall(re.compile(r'<a id="homepage1_HomePage.*href="//(.*?)">'), page)[0]
            title = re.findall(re.compile(r'<a id="homepage1_Home.*>(\D.*?)</a>'), page)[0]
            time = re.findall(re.compile(r'<a id="homepage1_Home.*>(\d.*?)</a>'), page)[0]
            content = re.findall(r'<div class="c_b_p_desc">([\S\s]*?)<a', page)[0]
            item = BlogspiderItem(url = url,title = title,time = time,content = content)
            yield item
        #next_page = re.findall(r'<a href="(.*?)">下一页</a>',response)  #翻页功能
        #if next_page:
         #   yield scrapy.Request(url = next_page[0],callback = self.parse)
            #Scrapy使用request对象来爬取web站点


