#coding = utf-8
#Version:Python-3.6.0
__date__ = '2018/3/30 22:49'
__author__ = 'colby'
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def get_one_page(url):
    requests_data={
        'kw': '天禾嘉泰',
        'pi': 'jingzan-leidaesf-sh_9-blog.csdn.net',
        'zpclkid': '0aae67b51a3a2953'
    }
    url=url + urlencode(requests_data)
    response = requests.get(url)
    if response.status_code=='302':
        print('请更换代理ip')
    else:
        soup=BeautifulSoup(response.text,'lxml')
        print(soup)

def main():
    url = 'http://nanchong.58.com/ershoufang/?key=%E5%A4%A9%E7%A6%BE%E5%98%89%E6%B3%B0'
    get_one_page(url)

if __name__=='__main__':
    main()
