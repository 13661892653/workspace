#coding=utf-8
#author:colby
import requests
from bs4 import BeautifulSoup

def request_index():
    response=requests.get("http://www.baidu.com")
    print(response)
    soup=BeautifulSoup(response.text,'lxml')
    print(soup.text)
    if response.status_code==200:
        print("访问百度网站正常")

def main():
    request_index()


if __name__ == "__main__":
    main()

