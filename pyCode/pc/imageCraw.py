#coding=utf-8
#爬取指定网站的所有图片
import re
import urllib.request

#返回指定url的html
def getHtmlstring(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
#根据传入的html，解析图片url地址，并且下载
def getImage(htmlstring,pagecnt):
    imageString=htmlstring.decode('utf-8')
    imagePattern = re.compile(r'lowsrc="(.*?\.jpg)"')
    imagehtml=re.findall(imagePattern,imageString)
    print(imagehtml)
for pagecnt in range(1,9):
    url="http://www.quanjing.com/search.aspx?q=%E6%B3%B0%E5%B1%B1||1|200|1|2||||#泰山||1|200"+"|%d|2||||" % (pagecnt)
    print(url)
    htmlstring=getHtmlstring(url)
    print(htmlstring)
    getImage(htmlstring,pagecnt)
    pagecnt+=1