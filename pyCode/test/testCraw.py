#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__date__ = '2018/1/3 16:15'
__author__ = "Colby"
import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    })
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com ')
print(response.read())