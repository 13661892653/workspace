#coding=utf-8
# 响应状态
# 200 代表成功
# 301	跳转
# 404	招不到网页
# 502	服务器错误
# javascript渲染加载
# from selenium import webdriver
# driver = webdriver.Chrome()
# dirver.get("http://m.weibo.com")
# pip install  chromedriver
import requests
from selenium import webdriver
response=requests.get("http://www.baidu.com")
print(response.headers)
driver = webdriver.Chrome()
driver.get("http://m.weibo.com")