#coding=utf-8
from bs4 import BeautifulSoup as bs
import urllib.request
import lxml
url='http://zdb.pedaily.cn'
openurl=urllib.request.urlopen(url)
html=openurl.read()
soup = bs(html,"lxml")
#print(soup)
#输出script标签所有内容
print(soup.script)
#输出script标签的标签名称
print(soup.script.name)
#输出script标签所有属性，以字典返回
print(soup.script.attrs)
#输出script标签的文本内容
print(soup.script.string)
#输出head标签的所有子标签，返回列表
print(soup.head.contents)
##输出head标签的所有子标签，返回生成器
children=soup.head.children
#打印生成器内容
print('生成器：')
for child in soup.head.children:
    print(child)
