# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderYouboyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provinceName=scrapy.Field()
    cityName=scrapy.Field()
    catagory_1_Name=scrapy.Field()
    catagory_1_Url=scrapy.Field()
    catagory_2_Name=scrapy.Field()
    catagory_2_Url=scrapy.Field()
    catagory_3_Name=scrapy.Field()
    catagory_3_Url=scrapy.Field()
    enterpriseName=scrapy.Field()
    contactPerson=scrapy.Field()
    enterpriseFax=scrapy.Field()
    enterprisePhone=scrapy.Field()
    enterpriseMobile=scrapy.Field()
    enterpriseAddr=scrapy.Field()
    enterpriseUrl=scrapy.Field()