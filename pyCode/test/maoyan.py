#coding=utf-8
# _author_: jingjing
# _date_: 2018/1/16
import requests as re
import urllib.request
from bs4 import BeautifulSoup
# 猫眼电影
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url='http://piaofang.maoyan.com/dashboard'
req = urllib.request.Request(url=url, headers=headers)
page=urllib.request.urlopen(req)
html=page.read()
print(html.decode("utf-8"))