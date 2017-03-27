#coding=utf-8
#爬取指定网站所有html链接地址
import re
import pymysql
import urllib.request
'''
#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=chaper_url, headers=headers)
    urllib.request.urlopen(req).read()
'''
#返回指定url的html，直接访问报错404，需要指定代理
def getHtmlstring(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    page=urllib.request.urlopen(req)
    html=page.read()
    print(html)
    return html

#解析网站的小说以及对应的网址
def getImage(url):
    imageString=getHtmlstring(url).decode('gb2312')
    imagePattern = re.compile(r'href="(.*?\.\w{3}/)">(.*?)</a>')
    imagehtml=re.findall(imagePattern,imageString)
    loaddb(imagehtml)

def loaddb(imagehtml):
    connDB1 = connDB()
    sql = "insert into craw_book(html,name) values"
    for i in imagehtml:
        sql1 = sql + '("' + i[0] + '","' + i[1] + '")'
        exeUpdate(connDB1[0], connDB1[1], sql1)
    connClose(connDB1[0], connDB1[1])

def connDB():
    # 连接数据库
    conn = pymysql.connect(host='172.16.33.252', user='root', passwd='root', db='xlh_craw', charset='utf8')
    cur = conn.cursor()
    return (conn, cur)

def exeUpdate(conn, cur, sql):
    # 更新语句，可执行Update，Insert语句
    sta = cur.execute(sql)
    conn.commit()
    return (sta)

def exeQuery(cur, sql):
    # 查询语句
    cur.execute(sql)
    result = cur.fetchone()
    return result

def connClose(conn, cur):
    # 关闭所有连接
    cur.close()
    conn.close()
#程序的入口
url="http://book.km.com/book_site.html"
main=getImage(url)
