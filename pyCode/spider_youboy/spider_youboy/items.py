# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderYouboyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    enterpriseName = scrapy.Field()
    provinceName=scrapy.Field()
    cityName = scrapy.Field()
    concactPerson = scrapy.Field()
    phoneNum = scrapy.Field()
    callNum = scrapy.Field()
    addrName = scrapy.Field()