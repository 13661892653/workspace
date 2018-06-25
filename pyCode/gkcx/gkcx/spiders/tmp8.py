# coding=utf-8
from multiprocessing.pool import Pool

from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import pymongo
import random

MONGO_URI='localhost'
MONGO_DATABASE='gkcx'


client=pymongo.MongoClient(MONGO_URI)
db=client[MONGO_DATABASE]

def get_tbody(driver,url):
    print ("正在访问",url)
    driver.get(url)
    # total = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'lxml')
    items = soup.select('tbody tr')
    if len(items)==0 or items==None:
        #print('正在重新',url)
        items=get_tbody(driver, url)
    return items

def get_gkcx_index(page):
    urls = ('https://gkcx.eol.cn/soudaxue/queryProvinceScore.html?page={}'.format(page) for page in
            range(page - 100 + 1, page))
    driver = webdriver.PhantomJS()
    #'PhantomJS'
    #totalPage='264064'
    driver.maximize_window()
    for url in urls:
        data={}
        items=get_tbody(driver,url)
        print('items',items)
        for item in items:
            item = item.find_all('td')
            data['_id'] = hash(item[0].a['href']+str(random.random()))
            data['学校网址'] = item[0].a['href']
            data['学校名称'] = item[0].a['title']
            data['招生地址'] = item[1].text
            data['文理科'] = item[2].text
            data['年份'] = item[3].text
            data['录取批次'] = item[4].text
            data['平均分'] = item[5].text
            data['省控线'] = item[6].text
            data['线差'] = item[7].text
            save_to_mongo(data)

def save_to_mongo(result):
    if result:
        if db['gkcx'].insert(result):
            print('插入成功',result)
            return True
        return False


def main(page):
    get_gkcx_index(page)

if __name__ == "__main__":
    pool = Pool()
    pool.map(main, [i * 50 for i in range(45, 50)])