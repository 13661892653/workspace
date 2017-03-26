#coding=utf-8
import re
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getImage(html):
    imageList = []
    for i in range(1,100):
        imageList.append('http://img1.mm131.com/pic/2299/%s.jpg' % i)
    j = 0
    #print[imageList]
    for i in imageList:
        urllib.request.urlretrieve(i, "D:\\pc\\2299\\%s.jpg" % j)
        j += 1
    return imageList
html=getHtml("http://www.mm131.com/xinggan/2292.html")
print(getImage(html))