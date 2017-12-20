#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
#from selenium.common.exceptions import
from selenium.webdriver.support.ui import WebDriverWait # available since
from selenium.webdriver.common.keys import Keys
from time import sleep
import os, time
driver = webdriver.Chrome()
print(u"加载驱动完成..")
driver.get("https://www.baidu.com")  # 加载页面
print(u"加载页面完成..")