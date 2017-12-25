#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"

import urllib
import urllib.request
from lxml import etree
import requests

def postData(url):
    posturl=url
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Request Method':'POST',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'SESSION=227e4457-3023-4f3a-97af-8ee3aaec6bda',
        'Host': 'crm.easyrong.dev:8080',
        'Origin': 'http://crm.easyrong.dev:8080',
        'Referer': 'http://crm.easyrong.dev:8080/crm/enterprisebank',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36',
    }
    postData={
        'memberPhone':'13661892653',
        'memberPwd':'xlh123456789',
    }
    postData = urllib.parse.urlencode(postData, encoding='utf-8').encode('utf-8')
    #postData = urllib.parse.urlencode(postData)
    #headers = urllib.parse.urlencode(headers)
    request = urllib.request.Request(url,data=postData,headers=headers)
    #request.get_method = lambda: 'HEAD'
    response = urllib.request.urlopen(request)
    text = response.read()
    print(text.decode('utf-8'))
    url='http://crm.easyrong.dev:8080/crm/enterprisebank'
    str=urllib.request.urlopen(url)
    res=str.read()
    print('res',res.decode('utf-8'))
if __name__=="__main__":
    url='http://crm.easyrong.dev:8080/login'
    postData(url)
