#coding=utf-8
#Version:Python-3.6.0
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyquery
import pymongo
import re
browser = webdriver.Chrome()
def search():
    try:
        browser.get('https://www.taobao.com/')
        input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        submit=WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.send_keys('python视频')
        submit.click()
        total=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        return total.text
    except TimeoutException:
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
    except TimeoutException:
        next_page(page_number)
def get_product():
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items item'))
    )
    html=browser.page_source
    doc=pyquery(html)
    items=doc('#mainsrp-itemlist .items item').items()
    for item in items:
        print(item)



def main():
    total=search()
    total=int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total+1):
        next_page(i)

if __name__=='__main__':
    main()