#coding=utf-8
#爬取整站html
import re
import urllib.request
import pymysql
import scrapy
from lxml import etree

def loaddb(data,v_htmlList):
    connDB1 = connDB()
    sql = "insert into craw_touzi(string1,string2,string3,string4,string5,string6,string7) values"
    for i in data:
        sql1 = sql + '("' + i[0] + '","' + i[1] + '","' + i[2]+ '","' + i[3]+ '","' + i[4]+ '","' + i[5]+'","'+v_htmlList+'")'
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

def gethtml(url):
    #获取指定url的html
    urlstr=urllib.request.urlopen(url)
    html=urlstr.read().decode('utf-8')
    return html
def getHtmlList(htmlstring):
    #获取指定html的网址列表
    htmlstring=htmlstring
    htmlpattern=re.compile(r'href="(.*?)">(.*?)</a><span class="split">/</span>')
    HtmlList=re.findall(htmlpattern,htmlstring)
    return HtmlList
def writeurl(htmlList):
    #网址写入文件F:\pythonFile\htmlList.txt
    htmlList=htmlList
    file1 = open('F:\\pythonFile\\htmlList.txt','w')
    number=1
    for i in htmlList:
        result=str(number)+'\t'+i[0]+'\t'+i[1]
        file1.write(result)
        file1.write("\n")
        number+=1
    file1.close()
def getData(htmlscript):
    selector = etree.HTML(htmlscript)
    dataList = selector.xpath('//*[@id="inv-list"]/li')
    print(dataList)
    result=dataList[1].xpath('string(.)'.split('\t'))
    print(result[1])
    return result
def writeData():
    pass

if __name__ == '__main__':
    url='http://zdb.pedaily.cn'
    htmlstring=gethtml(url)
    htmlList=getHtmlList(htmlstring)
    '''writeurl这一步暂停，后续放开，不要删除！'''
    #writeurl(htmlList)
    file=open('F:\\pythonFile\\htmlList.txt')
    htmlList=[]
    for fileread in file:
        #获取指定url的html脚本
        htmlList=fileread.split('\t')[1]
        page=1
        while 1:
            v_htmlList=htmlList+"%s" % page
            print(v_htmlList)
            htmlscript=gethtml(v_htmlList)
            data=getData(htmlscript)
            #loaddb(data,v_htmlList)
            page=page+1
    file.close()