#coding=utf-8
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("http://www.taobao.com")
# browser=webdriver.Firefox()
# browser=webdriver.Edge()
# browser=webdriver.PhantomJS()
# browser=webdriver.Safari()
input=browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(5)
input.clear()
input.send_keys('ipad')
button=browser.find_element_by_class_name('btn-search')
button.click()
browser.close()
