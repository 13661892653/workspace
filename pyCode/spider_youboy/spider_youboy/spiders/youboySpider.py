#coding=utf-8
'''
Tools:PyCharm 2017.1
Version:Python3.5
Author:colby_chen
Date:2017-09-26
'''
from scrapy import Request
#from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from .mysqldb import *
#import connClose,connDB,exeBath,exeQuery,exeUpdate
class novSpider(CrawlSpider):
    name="youboySpider"
    redis_key="youboySpider:start_urls"
    start_urls=['http://book.youboy.com/diqu.html']

    def parse_catagory_3(self, response):
        pass

    def parse_catagory_2(self, response):
        pass

    def parse_catagory_1(self,response):
        '''行业一级类目处理函数'''
        print('行业一级类目处理函数执行...')
        selector_catagory_1 = Selector(response)
        items=response.meta['items']
        provinceName = items['provinceName']
        cityName = items['cityName']
        cityUrl = items['cityUrl']
        # 大类
        catagory_1_List = selector_catagory_1.xpath('//div[@class="sheng_weizhi_con"]/ul[2]/li/a')
        for catagory_1 in catagory_1_List:
            catagory_1_Name = catagory_1.xpath('text()').extract()[0]
            catagory_1_Url = catagory_1.xpath('@href').extract()[0]
            print(provinceName, cityName, cityUrl, catagory_1_Name, catagory_1_Url)

    def parse(self,response):
        selector=Selector(response)
        url='http://book.youboy.com'
        #获取class="ybs-bcTitle"下所有的a标签
        diquUrl = []
        diqu1 = selector.xpath('//div[@class="ybs-bcTitle"]/a')
        for bg in diqu1:
            cityUrl = bg.xpath('@href').extract()[0]
            cityUrl=url+cityUrl
            cityName=bg.xpath('text()').extract()[0]
            print(cityName,cityName,cityUrl)
            diquUrl.append((cityName,cityName,cityUrl))
        diqu2 = selector.xpath('//div[@class="ybs-bcBody"]/ul/li')
        for bg in diqu2:
            provinceName=bg.xpath('h3/a/text()').extract()[0]
            cityList=bg.xpath('span/a')
            for city in cityList:
                cityName = city.xpath('text()').extract()[0]
                cityUrl = city.xpath('@href').extract()[0]
                cityUrl = url + cityUrl
                #print(provinceName,cityName,cityUrl)
                diquUrl.append((provinceName,cityName,cityUrl))
        #print(diquUrl)
        '''批量加载数据入库'''
        sql = "replace into youboy_diqu(provinceName,cityName,url) " \
              "values(%s,%s,%s)"
        connMysql = connDB()
        result = exeBath(connMysql[0], connMysql[1],sql,diquUrl)
        print('加载记录数:', result)
        connClose(connMysql[0], connMysql[1])

        #读取url，按省市分别处理
        sql = "select provinceName,cityName,url from youboy_diqu where provinceName='四川企业通讯录' and cityName='南充'"
        connMysql = connDB()
        result = exeQuery(connMysql[1],sql)
        print('result',result)
        print('正在处理%s %s的企业,URL为%s...' % (result[0],result[1],result[2]))
        connClose(connMysql[0], connMysql[1])
        print('result',result)
        items = {}
        items['provinceName'] = result[0]
        items['cityName'] = result[1]
        items['cityUrl'] = result[2]
        print('url',items['cityUrl'])
        yield Request(items['cityUrl'], meta={'items':items},callback=self.parse_catagory_1)