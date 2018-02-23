#coding=utf-8
from bs4 import BeautifulSoup

with open('the_blah.html','r') as wb_data:
    Soup=BeautifulSoup(wb_data,'lxml')
    images=Soup.select('body > div.main-content > ul > li > img')
    for i in images:
        print(i)