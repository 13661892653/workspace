#coding=utf-8
import urllib.request
from lxml import etree
import pymysql
from datetime import datetime

def connDB():
    # 连接数据库
    conn = pymysql.connect(host='172.16.33.252', user='root', passwd='root', db='xlh_craw', charset='utf8')
    cur = conn.cursor()
    return (conn, cur)
def exeUpdate(conn, cur, sql):
    '''更新语句，可执行Update，Insert语句'''
    sta = cur.execute(sql)
    conn.commit()
    return (sta)
def exeBath(conn, cur, sql,data):
    '''批量插入数据'''
    sta = cur.executemany(sql,data)
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
def getHtml(url):
    try:
        openurl=urllib.request.urlopen(url)
        html=openurl.read()
        return html
    except Exception as e:
        return '网络超时'
    #print(html)
def defSql(jobType):
    if jobType=='people':
        sql = "insert into craw_people(image,name,enterprise, job,type, description) values(%s,%s,%s,%s,%s,%s)"
    return sql
def listTransList(list):
    return ''.join(list)
def getDataColumn(selector,pagesize):
    list = []
    for i in range(1, pagesize):
        image= listTransList(selector.xpath('//*[@id="people-list"]/li[' + str(i) + ']/div[1]/a/img/@src'))
        name = listTransList(selector.xpath('//*[@id="people-list"]/li[' + str(i) + ']/div[2]/h3/a/text()'))
        enterprise = listTransList(selector.xpath('//*[@id="people-list"]/li[' + str(i) + ']/div[2]/h3/span/text()[1]'))
        job = listTransList(selector.xpath('//*[@id="people-list"]/li[' + str(i) + ']/div[2]/h3/span/text()[2]'))
        type = listTransList(selector.xpath('//*[@id="people-list"]/li[' + str(i) + ']/div[2]/div[1]/a/text()'))
        description = listTransList(selector.xpath('//*[@id="people-list"]/li[' + str(i) + ']/div[2]/div[2]/text()'))
        data = (image,name, enterprise, job,type, description)
        list.append(data)
    return list
def getData(html):
    selector = etree.HTML(html)
    '''获取每页行数'''
    dataList=selector.xpath('//*[@id="people-list"]/li')
    pagesize=len(dataList)+1
    list =getDataColumn(selector,pagesize)
    return list
def loaddata(sql,data):
    connMysql = connDB()
    exeBath(connMysql[0], connMysql[1], sql,data)
    connClose(connMysql[0], connMysql[1])
def dateFormat(date):
    datestring=datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S.%f")
    return datestring

if __name__=="__main__":
    '''定义主页入口'''
    startTime=dateFormat(datetime.now())
    print('程序已经开始，时间为：',startTime)
    initurl='http://zdb.pedaily.cn/people/all/'
    errTime=0
    '''获取html'''
    for i in range(1,10000):
        if i==1:
            url=initurl
        else:
            url='http://zdb.pedaily.cn/people/all/%s/' % i
        print('当前url地址：',url)
        html=getHtml(url)
        if html=='网络超时':
            break
        '''根据url拿取数据'''
        data=getData(html)
        if data==[]:
            errTime+=1
            if errTime>4:
                endTime=dateFormat(datetime.now())
                print('Game Over!!!')
                print('程序开始时间：', startTime)
                print('程序结束时间：', endTime)
                break
        '''根据类型提取sql'''
        sql=defSql('people')
        '''数据入库'''
        loaddata(sql,data)
        print(dateFormat(datetime.now()),'-->',data)