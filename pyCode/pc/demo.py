#coding=utf-8
"""抓取百度首页的html代码"""
import urllib.request
import re
req=urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(req)
#print(response.read())
s='chen,zhang,li,zhao,bi'
pa=r'^chen'
pa1=r'bi$'
pa2=r'[abc]'
pa3=r'zha[on]'
print(re.findall(pa,s))
print(re.findall(pa1,s))
print(re.findall(pa2,s))
print(re.findall(pa3,s))
phone='0817-3447210'
#pa4=r'[0-9]{3,4}-[0-9]{7,8}'
pa5=r'^[0-9]*-[0-9]*$'
print(re.findall(pa5,phone))