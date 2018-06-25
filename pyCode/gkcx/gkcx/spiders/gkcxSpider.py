# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import pymongo


class GkcxspiderSpider(scrapy.Spider):
    name = 'gkcxSpider'
    allowed_domains = ['gkcx.eol.cn']
    start_urls = ['https://gkcx.eol.cn/soudaxue/queryProvince.html']
    #start_urls = ['https://gkcx.eol.cn/soudaxue/queryProvinceScore.html?messtype=jsonp&callback=jQuery183016283849677265239_1529835184811&provinceforschool=&schooltype=&page=1&size=10&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&_=1539835185047']
    def parse(self, response):
        res=response.text
        print(res)
