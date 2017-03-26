#coding=utf-8
import re
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getImage(html):
    reg=r'src="(.*?\.jpg)"'
    img=re.compile(reg)
    html = html.decode('utf-8')
    imageList=re.findall(img,html)
    j=0
    for i in imageList:
        urllib.request.urlretrieve(i,"D:\\pc\\%s.jpg" % j)
        j+=1
    return imageList
html=getHtml("http://www.mm131.com/")
print(getImage(html))