#coding=utf-8
import requests
import pymongo

from  bs4 import BeautifulSoup
from  conf.config import *
from  multiprocessing import Pool

client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

proxy = None
max_count=5
count=0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/24.0'}

def get_proxy():
    print('正在获取代理...')
    try:
        proxy_pool_url='http://127.0.0.1:5555/random'
        response=requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return  None
    except ConnectionError:
        return None

def parse_index(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select(".table-plate3")
    for item in items:
        data = {}
        data['projectUrl'] = item.select('.tp1 a')[0].attrs['href']
        data['titleImg'] = item.select('.tp1 a img')[0].attrs['src']
        data['projectName'] = item.select('.tp2 .tp2_tit a')[0].get_text()
        data['enterpriseName'] = item.select('.tp2 .tp2_com')[0].get_text()
        data['amt'] = item.select('.tp-mean .money')[0].get_text()
        # 获取第7个节点
        data['turn'] = item.contents[7].get_text()
        data['Investors'] = item.select('.tp3')[0].attrs['title']
        data['Industry'] = item.contents[11].get_text()
        data['Date'] = item.contents[13].get_text()
        data['detailUrl'] = item.contents[15].select('a')[0].attrs['href']
        save_to_mongo(data)

def get_html(page,count=1):
    global proxy
    url = 'http://www.cyzone.cn/event/list-764-0-%s-0-0-0-0/' %(page)
    print('42',url)
    if count == max_count:
        print('重试次数大于5次了。')
        return None
    try:
        if proxy:
            print('代理存在')
            proxies = {
                'http': 'http://' + proxy
            }
            print('proxies',proxies)
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            print('代理为NoneType，正在重新获取')
            proxy = get_proxy()
            print('proxy', proxy)
            count += 1
            return get_html(page, count)
        if response.status_code == 200:
            print('当前状态正常。')
            print("-->>当前页码%s" %page)
            return response.text
        # if response.status_code == 302:
        #     print('Response status:302')
        #     proxy = get_proxy()
        #     if proxy:
        #         print('正在使用代理：', proxy)
        #         return get_html(url)
        #     else:
        #         print('代理获取失败...')
        #         return None
    except Exception:
        print('代理获取异常，正在重新获取')
        proxy = get_proxy()
        print('proxy',proxy)
        count += 1
        return get_html(page, count)

def main(page):
    for i in range(page-10+1,page-1):
        html=get_html(i,count)
        parse_index(html)

def save_to_mongo(result):
    if result:
        if db[MONGO_TABLE].insert(result):
            print('插入成功')
            return True
        return False
if __name__ == "__main__":
    pool = Pool()
    pool.map(main, [i * 10 for i in range(2,123)])
