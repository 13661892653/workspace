#coding=utf-8
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery

def main(page):
    get_one_data(page)

def get_one_data(page):
    url = 'http://www.cyzone.cn/event/list-764-0-%s-0-0-0-0/' %(int(page))
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    items=soup.select(".table-plate3")
    for item in items:
        data={}
        data['projectUrl'] = item.select('.tp1 a')[0].attrs['href']
        data['titleImg'] = item.select('.tp1 a img')[0].attrs['src']
        data['projectName'] = item.select('.tp2 .tp2_tit a')[0].get_text()
        data['enterpriseName'] = item.select('.tp2 .tp2_com')[0].get_text()
        data['amt'] = item.select('.tp-mean .money')[0].get_text()
        #获取第7个节点
        data['turn'] = item.contents[7].get_text()
        data['Investors'] = item.select('.tp3')[0].attrs['title']
        data['Industry'] = item.contents[11].get_text()
        data['Date'] = item.contents[13].get_text()
        data['detailUrl'] = item.contents[15].select('a')[0].attrs['href']
        print(data)

if __name__ == "__main__":
    for i in range(1,1226):
        main(i)
