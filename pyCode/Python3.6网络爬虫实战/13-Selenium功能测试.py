#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser=webdriver.Chrome()
try:
    browser.get("http://www.baidu.com")
    #根据id查找节点
    input=browser.find_element_by_id('kw')
    input.send_keys("python")
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(expected_conditions.presence_of_all_elements_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()