#coding=utf-8
"""抓取百度首页的html代码"""
import urllib.request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url="http://www.qingtaoke.com/qingsou?cat=12&s_type=1&sort=1"
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
page=response.read()
print(page)
