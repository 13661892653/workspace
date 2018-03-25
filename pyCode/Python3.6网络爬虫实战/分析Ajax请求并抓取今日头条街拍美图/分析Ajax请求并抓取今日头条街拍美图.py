#coding=utf-8
import requests
import pymongo
import re
import json
import ast
from requests.exceptions import RequestException
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from multiprocessing import Pool
from config import *

client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

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
    response = requests.get(url)
    return response.text
def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    headers = {
        'authority': 'www.toutiao.com',
        'method': 'GET',
        'path': '/api/article/user_log/?c=detail_gallery&sid=2iym24ada1521603062308&type=close&st=446784&t=1521603509092',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'tt_webid=6531929919109285390; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16218bc702a740-076efe0189c54b-454c062c-1fa400-16218bc702b2ec; tt_webid=6531929919109285390; uuid="w:050d6218374e42b8866bf4e167727989"; _ga=GA1.2.1295836644.1521445623; sso_login_status=0; CNZZDATA1259612802=701175850-1520831231-%7C1521598838; __tasessionId=2iym24ada1521603062308',
        'referer': 'https://www.toutiao.com/a6398112018415681793/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
    }
    #print('url',url)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错！')
        return None

def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')
    #print('soup',soup)
    title = soup.select('title')
    if title.__len__()!=0:
        title=title[0].get_text()
        #title=soup.select('title')[0].get_text()
        #print('title',title)
        images_pattern=re.compile('gallery: JSON.parse\((.*?)\),',re.S)
        result=re.search(images_pattern,html)
        #print('result',result)
        if result:
            #print('result',result.group(1))
            json_data=json.loads(result.group(1))
            json_data=ast.literal_eval(json_data)
            #print('dataType', type(json_data))
            #print('data',data,type(data))
            if json_data and 'sub_images' in json_data.keys():
                sub_images=json_data.get('sub_images')
                #print('sub_images',sub_images)
                images=[item.get('url') for item in sub_images]
                return {
                    'title':title,
                    'url':url,
                    'image':images
                }
def save_to_mongo(result):
    if result:
        if db[MONGO_TABLE].insert(result):
            print('插入成功')
            return True
        return False
def main(offset):
    html=get_page_index(0,'美女')
    print('上海',html)
    for url in parse_page_index(html):
        if url:
            html=get_page_detail(url)
            #print('html',html)
            if html:
                result=parse_page_detail(html,url)
                print('result',result)
                save_to_mongo(result)

if __name__=="__main__":
    #启用多线程
    pool=Pool()
    pool.map(main,[i*10 for i in range(20)])
