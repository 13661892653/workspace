#coding=utf-8
'''
Tools:PyCharm 2017.1
Version:Python3.5
Author:colby_chen
Date:2017-09-26
'''
import copy

from scrapy import Request
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from .mysqldb import *
#import connClose,connDB,exeBath,exeQuery,exeUpdate
class youboySpider(CrawlSpider):
    name="youboySpider"
    redis_key="youboySpider:start_urls"
    start_urls=['http://book.youboy.com/diqu.html']
    def parse_catagory_3(self,response):
        '''行业三级类目处理函数'''
        '''行业二级类目处理函数'''
        selector_catagory_3 = Selector(response)
        items_catagory_3 = response.meta['items_catagory_2']
        print('二级类目', items_catagory_3['catagory_2_Name'])
        catagory_3_List = selector_catagory_3.xpath('//div[@class="sheng_weizhi_con"]/ul[2]/li/a')
        data=[]
        for catagory_3 in catagory_3_List:
            catagory_3_Name = catagory_3.xpath('text()').extract()[0]
            catagory_3_Url = catagory_3.xpath('@href').extract()[0]
            items_catagory_3['catagory_3_Name'] = catagory_3_Name
            items_catagory_3['catagory_3_Url'] = items_catagory_3['url'] + catagory_3_Url
            #print(items_catagory_3['provinceName'],items_catagory_3['cityName'],items_catagory_3['catagory_1_Name'],items_catagory_3['catagory_1_Url'],items_catagory_3['catagory_2_Name'],items_catagory_3['catagory_2_Url'],items_catagory_3['catagory_3_Name'],items_catagory_3['catagory_3_Url'])
            #yield Request(items_catagory_2['catagory_2_Url'], meta={'items_catagory_2': items_catagory_2},callback=self.parse_catagory_3)
            data.append((items_catagory_3['provinceName'],items_catagory_3['cityName'],items_catagory_3['catagory_1_Name'],items_catagory_3['catagory_1_Url'],items_catagory_3['catagory_2_Name'],items_catagory_3['catagory_2_Url'],items_catagory_3['catagory_3_Name'],items_catagory_3['catagory_3_Url']))

        '''行业数据批量加载数据入库'''
        sql = "replace into youboy_enterprise(provinceName,cityName,catagory_1_Name,catagory_1_Url,catagory_2_Name,catagory_2_Url,catagory_3_Name,catagory_3_Url) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s)"
        connMysql = connDB()
        result = exeBath(connMysql[0], connMysql[1], sql, data)
        # print('加载记录数:', result)
        connClose(connMysql[0], connMysql[1])

    def parse_catagory_2(self, response):
        '''行业二级类目处理函数'''
        selector_catagory_2 = Selector(response)
        items_catagory_2 = response.meta['items_catagory_1']
        print('一级类目', items_catagory_2['catagory_1_Name'])
        catagory_2_List = selector_catagory_2.xpath('//div[@class="sheng_weizhi_con"]/ul[2]/li/a')
        for catagory_2 in catagory_2_List:
            catagory_2_Name = catagory_2.xpath('text()').extract()[0]
            catagory_2_Url = catagory_2.xpath('@href').extract()[0]
            items_catagory_2['catagory_2_Name'] = catagory_2_Name
            items_catagory_2['catagory_2_Url'] = items_catagory_2['url'] + catagory_2_Url
            print(items_catagory_2['provinceName']
                  ,items_catagory_2['cityName']
                  ,items_catagory_2['catagory_1_Name']
                  ,items_catagory_2['catagory_1_Url']
                  ,items_catagory_2['catagory_2_Name']
                  ,items_catagory_2['catagory_2_Url'])
            yield Request(items_catagory_2['catagory_2_Url'], meta={'items_catagory_2': items_catagory_2}, callback=self.parse_catagory_3)

    def parse_catagory_1(self,response):
        '''行业一级类目处理函数'''
        selector_catagory_1 = Selector(response)
        items_catagory_1=response.meta['items']
        # 大类
        print('当前地区',items_catagory_1['provinceName'],items_catagory_1['cityName'])
        catagory_1_List = selector_catagory_1.xpath('//div[@class="sheng_weizhi_con"]/ul[2]/li/a')
        if catagory_1_List.__len__() ==0:
            catagory_1_List = selector_catagory_1.xpath('//div[@class="sheng_weizhi_con"]/ul/li/a')
        for catagory_1 in catagory_1_List:
            items_catagory_1['catagory_1_Name'] = catagory_1.xpath('text()').extract()[0]
            items_catagory_1['catagory_1_Url'] = items_catagory_1['url']+catagory_1.xpath('@href').extract()[0]
            yield Request(items_catagory_1['catagory_1_Url'], meta={'items_catagory_1':copy.deepcopy(items_catagory_1)}, callback=self.parse_catagory_2)
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
            #print(cityName,cityName,cityUrl)
            diquUrl.append((cityName,cityName,cityUrl,'Y'))
        diqu2 = selector.xpath('//div[@class="ybs-bcBody"]/ul/li')
        for bg in diqu2:
            provinceName=bg.xpath('h3/a/text()').extract()[0]
            cityList=bg.xpath('span/a')
            for city in cityList:
                cityName = city.xpath('text()').extract()[0]
                cityUrl = city.xpath('@href').extract()[0]
                cityUrl = url + cityUrl
                #print(provinceName,cityName,cityUrl)
                diquUrl.append((provinceName,cityName,cityUrl,'Y'))
        #print(diquUrl)
        '''批量加载数据入库'''
        sql = "replace into youboy_diqu(provinceName,cityName,url,flag) " \
              "values(%s,%s,%s,%s)"
        connMysql = connDB()
        result = exeBath(connMysql[0], connMysql[1],sql,diquUrl)
        #print('加载记录数:', result)
        connClose(connMysql[0], connMysql[1])


        #############################################################################################################
        #############################################################################################################
        #############################################################################################################
        #读取url，按省市分别处理
        selectsql = "select provinceName,cityName,url from youboy_diqu where flag='Y'"
        connMysql = connDB()
        results = exeQuery(connMysql[1],selectsql)
        # updatesql = "update youboy_diqu set flag='N' where provinceName='%s' and cityName='%s'" %(result[0],result[1])
        # updateresult = exeUpdate(connMysql[0],connMysql[1], updatesql)
        connClose(connMysql[0], connMysql[1])
        for result in results:
            print('当前地区%s-%s' %(result[0],result[1]))
            items = {}
            items['provinceName'] = result[0]
            items['cityName'] = result[1]
            items['cityUrl'] = result[2]
            items['url']=url
            #print('url',items['cityUrl'])
            yield Request(items['cityUrl'], meta={'items':copy.deepcopy(items)},callback=self.parse_catagory_1)