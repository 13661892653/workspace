#coding=utf-8
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import pymongo
import re
from multiprocessing import Pool
import json

def get_page_index(offset,keyword):
    requests_data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url='https://www.toutiao.com/search_content/?' + urlencode(requests_data)
    # try:
    #     response=requests.get(url)
    #     if response.status_code == 200:
    #         return response.text
    #     return None
    # except RequestException:
    #     print('请求索引页出错！')
    #     return None
    response = requests.get(url)
    return response.text
def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    print('url',url)
    try:
        response=requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错！')
        return None

def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')
    print('soup',soup)
    title=soup.select('title')[0].get_text()
    print(title)
    images_pattern=re.compile('gallery: JSON.parse("(.*?)"),',re.S)
    result=re.search(images_pattern,html)
    if result:
        data=json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            return {
                'title':title,
                'url':url,
                'image':images
            }

def main():
    html=get_page_index(0,'风景')
    print('南充',html)
    for url in parse_page_index(html):
        if url:
            html=get_page_detail(url)
            print('html',html)
            # if html:
            #     result=parse_page_detail(html,url)
            #     print('result',result)

if __name__=="__main__":
    # pool=Pool()
    # pool.map(main,[i*10 for i in range(10)])
    main()
