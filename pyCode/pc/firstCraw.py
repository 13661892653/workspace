#coding=utf-8
#chenlun的第一个爬虫程序
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
        imgname=re.search(r'\d{4,5}',i).group(0)
        print(imgname)
        urllib.request.urlretrieve(i,imgname+".jpg")
    return imageList
html=getHtml("http://bizhitest.quanjing.com/topic/930_13_bar-0105")
print(getImage(html))
