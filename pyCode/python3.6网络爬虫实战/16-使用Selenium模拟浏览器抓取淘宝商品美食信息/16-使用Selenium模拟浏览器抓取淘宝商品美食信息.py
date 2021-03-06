#coding=utf-8
#Version:Python-3.6.0
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery
import pymongo
import re
from config import *

browser = webdriver.Chrome()
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

def search():
    try:
        browser.get('https://www.taobao.com/')
        input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        submit=WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.send_keys('婴儿用品')
        submit.click()
        total=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        print('超时啦.............',TimeoutException)
        return search()


def next_page(page_number):
    try:
        input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        submit = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number))
        )
        get_products()
    except TimeoutException:
        print('超时啦.............')
        next_page(page_number)


def get_products():
    print("正在获取详情信息...")
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item'))
    )
    html=browser.page_source
    doc=PyQuery(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            '首图': item.find('.pic .img').attr('src'),
            '价格': item.find('.price').text().replace('\n',' '),
            '购买人数': item.find('.deal-cnt').text()[0:-3],
            '宝贝标题': item.find('.title').text().replace('\n',' '),
            '店铺名称': item.find('.shop').text(),
            '店铺位置': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    if result:
        if db[MONGO_TABLE].insert(result):
            print('插入成功')
            return True
        return False


def main():
    total=search()
    total=int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total+1):
        next_page(i)

if __name__=='__main__':
    main()