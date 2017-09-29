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
#from scrapy.spiders import CrawlSpider
from scrapy_redis.spiders import RedisSpider
from .mysqldb import connClose,connDB,exeBath,exeQuery,exeUpdate
import urllib.request
from lxml import etree
from ..items import SpiderYouboyItem
def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

def getPage(url):
    '''
    根据传过来的url，获取所有分页，并返回一个url列表
    :param url:
    :return:
    '''
    urlList=[]
    startUrl=url
    html=gethtml(startUrl)
    selector=etree.HTML(html)
    nextPageFlag=selector.xpath('//dl[@class="sheng_weizhi_next01"]/a[last()]/text()')
    print('nextPageFlag',nextPageFlag)
    maxPage=None
    if nextPageFlag.__len__()>0:
        endurl=url+'10000'
        endhtml=gethtml(endurl)
        maxPage = selector.xpath('//dl[@class="sheng_weizhi_next01"]/strong/text()')[0]
        print('maxPage', maxPage)
        for i in range(1,int(maxPage)+1):
            currentUrl=url+str(i)
            print('currentUrl',currentUrl)
            urlList.append(currentUrl)
    else:
        urlList.append(startUrl)
    print('urlList...............................................', urlList)
    return urlList

def enterpriseContentDetail(enterpriseUrl,*args,**kwargs):
    page = urllib.request.urlopen(enterpriseUrl)
    html = page.read().decode('utf-8')
    selector = etree.HTML(html)
    # enterpriseContent = selector.xpath('//div[@class="txl_content_con"]/ul[1]/')
    # print('enterpriseContent', enterpriseContent)
    enterpriseDetail = []
    enterpriseName = selector.xpath('//div[@class="txl_content_con"]/ul[1]/h1/text()')[0].replace('\t','').replace('\r\n','')
    contactPerson = selector.xpath('//div[@class="txl_content_con"]/ul[1]/li[2]/text()')[0].replace('\t','').replace('\r\n','')
    enterpriseFax = selector.xpath('//div[@class="txl_content_con"]/ul[1]/li[3]/text()')[0].replace('\t','').replace('\r\n','')
    enterprisePhone = selector.xpath('//div[@class="txl_content_con"]/ul[1]/li[4]/text()')[0].replace('\t','').replace('\r\n','')
    enterpriseMobile = selector.xpath('//div[@class="txl_content_con"]/ul[1]/li[5]/text()')[0].replace('\t','').replace('\r\n','')
    enterpriseAddr = selector.xpath('//div[@class="txl_content_con"]/ul[1]/li[6]/text()')[0].replace('\t','').replace('\r\n','')
    enterpriseUrl=enterpriseUrl
    base=list(*args)
    enterpriseDetail = [enterpriseName,contactPerson,enterpriseFax,enterprisePhone,enterpriseMobile,enterpriseAddr,enterpriseUrl]
    if enterpriseDetail.__len__() == 0:
        enterpriseDetail = ['', '', '', '', '', '',enterpriseUrl]
    base.extend(enterpriseDetail)
    return base

class youboySpider(RedisSpider):
    name="youboySpider"
    redis_key="youboySpider:start_urls"
    start_urls=['http://book.youboy.com/diqu.html']
    def enterpriseContent(self,response):
        '''企业列表处理'''
        select_enterpriseList = Selector(response)
        items_enterpriseList = response.meta['baseInfo2']
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        enterpriseList = select_enterpriseList.xpath('//*[@id="content"]/ul/div/strong/a')
        provinceName = items_enterpriseList['provinceName']
        cityName = items_enterpriseList['cityName']
        catagory_1_Name = items_enterpriseList['catagory_1_Name']
        catagory_1_Url = items_enterpriseList['catagory_1_Url']
        catagory_2_Name = items_enterpriseList['catagory_2_Name']
        catagory_2_Url = items_enterpriseList['catagory_2_Url']
        catagory_3_Name = items_enterpriseList['catagory_3_Name']
        catagory_3_Url = items_enterpriseList['catagory_3_Url']
        baseInfo = [provinceName, cityName, catagory_1_Name, catagory_1_Url, catagory_2_Name, catagory_2_Url,
                    catagory_3_Name, catagory_3_Url]
        enterpriseContentList = []
        if enterpriseList.__len__()==0:
            items_enterpriseList['enterpriseName']=''
            items_enterpriseList['contactPerson']=''
            items_enterpriseList['enterpriseFax']=''
            items_enterpriseList['enterprisePhone']=''
            items_enterpriseList['enterpriseMobile']=''
            items_enterpriseList['enterpriseAddr']=''
            items_enterpriseList['enterpriseUrl']=''
            #enterpriseContentDict=[(provinceName,cityName,catagory_1_Name,catagory_1_Url,catagory_2_Name,catagory_2_Url,catagory_3_Name,catagory_3_Url,'','','','','','','')]
        for enterpriseInfo in enterpriseList:
            enterpriseUrl=enterpriseInfo.xpath('@href').extract()[0]
            enterpriseContent=enterpriseContentDetail(enterpriseUrl,baseInfo)
            items_enterpriseList['enterpriseName'] = enterpriseContent[8]
            items_enterpriseList['contactPerson'] = enterpriseContent[9]
            items_enterpriseList['enterpriseFax'] = enterpriseContent[10]
            items_enterpriseList['enterprisePhone'] = enterpriseContent[11]
            items_enterpriseList['enterpriseMobile'] = enterpriseContent[12]
            items_enterpriseList['enterpriseAddr'] = enterpriseContent[13]
            items_enterpriseList['enterpriseUrl'] = enterpriseContent[14]
            yield items_enterpriseList

        # sql = "replace into youboy_enterprise(provinceName,cityName,catagory_1_Name,catagory_1_Url,catagory_2_Name,catagory_2_Url,catagory_3_Name,catagory_3_Url" \
        #       ",enterpriseName,contactPerson,enterpriseFax,enterprisePhone,enterpriseMobile,enterpriseAddr,enterpriseUrl) " \
        #       "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # connMysql = connDB()
        # result = exeBath(connMysql[0], connMysql[1], sql, enterpriseContentList)
        # connClose(connMysql[0], connMysql[1])

    def parse_enterpriseFirstPage(self, response):
        '''企业列表处理'''
        select_enterpriseList=Selector(response)
        baseInfo2 = response.meta['items_catagory_3']
        firstPage = baseInfo2['catagory_3_Url']
        pageList=getPage(firstPage)
        for pageurl in pageList:
            '''
            dont_filter=True 多层循环失效加上此参数
            '''
            yield Request(pageurl,meta={'baseInfo2':copy.deepcopy(baseInfo2)},callback=self.enterpriseContent,dont_filter=True)

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
            yield Request(items_catagory_3['catagory_3_Url'], meta={'items_catagory_3': copy.deepcopy(items_catagory_3)}
                          ,callback=self.parse_enterpriseFirstPage)
            #data.append((items_catagory_3['provinceName'],items_catagory_3['cityName'],items_catagory_3['catagory_1_Name'],items_catagory_3['catagory_1_Url'],items_catagory_3['catagory_2_Name'],items_catagory_3['catagory_2_Url'],items_catagory_3['catagory_3_Name'],items_catagory_3['catagory_3_Url']))

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
            yield Request(items_catagory_2['catagory_2_Url'], meta={'items_catagory_2': copy.deepcopy(items_catagory_2)}, callback=self.parse_catagory_3)

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
        selectsql = "select provinceName,cityName,url from youboy_diqu where provinceName='上海' and cityName='上海' and flag='Y'"
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