#coding=utf-8
import re
import urllib.request
import datetime
import unicodedata
from lxml import etree
#from multiprocessing.dummy import Pool as ThreadPool
import pymysql
def loaddb(data):
    connDB1 = connDB()
    sql = "insert into rt114(html) values"
    sql1 = sql + '("' + data + '")'
    print(sql1)
    exeUpdate(connDB1[0], connDB1[1], sql1)
    connClose(connDB1[0], connDB1[1])
def writefile(content):
    file_object = open('D:\\\pc\\imagefile.txt', 'a')
    file_object.write(content+'\n')
    file_object.close()
def connDB():
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='mysql', db='craw', charset='utf8')
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
def unicode_to_string(types):
    try:
        types = unicodedata.normalize("NFKD", types).encode('ascii', 'ignore')
        return types
    except:
        return types
def gethtml(url):
    try:
        page=urllib.request.urlopen(url)
        html=page.read().decode('utf-8')
        return html
    except Exception as e:
        return 'ERROR'
def getHtmlList(html):
    selector = etree.HTML(html)
    content = selector.xpath('/html/body/div[1]/div/div[2]/ul/li/a/@href')
    del content[0]
    return content
def getDeHtmlList(htmlDetail):
    selector = etree.HTML(unicode_to_string(htmlDetail))
    content = selector.xpath('/html/body/div[2]/ul/li/a/@href')
    return content

def getDePageSize(htmlDetail):
    selector = etree.HTML(unicode_to_string(htmlDetail))
    dePageSize = selector.xpath('/html/body/div[2]/nav/ul/li[last()]/a/text()')
    print(dePageSize)
    return dePageSize[0]
def getDePageSizeThird(htmlDetail):
    try:
        selector = etree.HTML(htmlDetail)
        dePageSize = selector.xpath('/html/body/nav/ul/li[last()]/a/text()')
        print(dePageSize)
        return dePageSize[0]
    except Exception as e:
        return -1
def getImage(third,firstname):
    for r in third:
        imagehtml = gethtml(r)
        try:
            selector = etree.HTML(unicode_to_string(imagehtml))
            content = selector.xpath('/html/body/div[3]/a/img/@src')[0]
            # print(content)
            fname = re.findall(r'https://(.*?)/(.*?)/(.*?)/(.*?).jpg', content)
            print(fname[0][1], fname[0][2], fname[0][3])
            fname = firstname + '_' + fname[0][1] + '_' + fname[0][2] + '_' + fname[0][3]
            # print('正在获取文件：',fname)
            # print(content)
            # writefile(content)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), firstname, content)
            urllib.request.urlretrieve(content, "D:\\pc\\%s.jpg" % fname)
        except Exception as e:
            print("抓取图像异常！！！",e)
            continue
if __name__=='__main__':
    url='https://www.renti114.net/'
    html=gethtml(url)
    htmlList=getHtmlList(html)
    #获取图片国际分类
    for i in htmlList:
        firstname = re.findall(r'https://www.renti114.net/(.*?)/',i)[0]
        print(firstname)
        htmlDetail = gethtml(i)
        dePageSize = getDePageSize(htmlDetail)
        print(dePageSize)
        second = [i]
        # 获取图片国际分类所有分页url
        for j in range(2,int(dePageSize)+1):
            html=i+'index_%d.html'%j
            second.append(html)
        print(second)
        #获取所有分页的
        for k in second:
            #获取url的html
            htmlDetail = gethtml(k)
            deHtmlList=getDeHtmlList(htmlDetail)
            print(deHtmlList)
            #第三级页面List
            for m in deHtmlList:
                htmlDetail = gethtml(m)
                dePageSize = getDePageSizeThird(htmlDetail)
                print(dePageSize)
                third = [m]
                # 获取图片国际分类所有分页url
                for n in range(2, int(dePageSize) + 1):
                    string='_'+str(n)+'.'
                    html = re.sub('\.html','%shtml'%string,m,re.S)
                    third.append(html)
                getImage(third,firstname)


