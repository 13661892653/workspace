#coding=utf-8
#author:colby

import requests
from bs4 import BeautifulSoup
import json
import settings
import pymongo
from settings import *
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

url='http://mikecrm.com/handler/web/form_submit/handleGetListFormSubmitSummary.php?d=%7B%22cvs%22%3A%7B%22i%22%3A{id}%7D%7D'
next_url ='http://mikecrm.com/handler/web/form_submit/handleGetListFormSubmit_all.php?d=%7B%22cvs%22%3A%7B%22i%22%3A{id}%2C%22nxt%22%3A{next}%7D%7D'
id='1706628'
Cookie='_ga=GA1.2.650401320.1506760585; _gid=GA1.2.186151230.1529371753; PHPSESSID=jkeg3hal269r2bp7c1sk8spqq3; uvi=3QHegvbWHI5bPjtfk2i1ajnxo3BfrM8uANJOiUKYBN9q7C01; _gat=1'

request_headers={
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':Cookie,
    'Host': 'mikecrm.com',
    'Origin': 'http://mikecrm.com',
    'Referer': 'http://mikecrm.com/form.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_first_json():
    first_url=url.format(id=id)
    resonse=requests.get(first_url,headers=request_headers)
    soup=BeautifulSoup(resonse.text,'lxml')
    json_data=json.loads(soup.text)
    items=parse_json(json_data)

def parse_json(json_data):
    items={}
    datas = json_data['list']['d']
    date_list = json_data['list']['mp_fsCA']
    next_page_url = json_data['list']['nxt']
    for data in datas:
        name_list=[]
        name_cnt=len(data[4]['cp'])-5
        items['id']=data[0]
        items['name'] = data[4]['cp']['1279214']['n']
        items['phone'] = data[4]['cp']['1279215'][0]
        for cnt in range(0,name_cnt):
            index=1279217 + cnt * 3
            name=data[4]['cp'].get(str(index))
            if name:
                name_list.append(name)
        items['enterprise_name'] = name_list
        items['date'] = date_list[str(items['id'])]
        save_to_mongodb(items)

    if next_page_url:
        print('next_page_url',next_page_url)
        parse_many_json(next_page_url)

def parse_many_json(next):
    next_page_url = next_url.format(id=id,next=next)
    resonse = requests.get(next_page_url, headers=request_headers)
    soup = BeautifulSoup(resonse.text, 'lxml')
    json_data = json.loads(soup.text)
    #print('json_data',json_data)
    items = parse_json(json_data)

def save_to_mongodb(item):
    if item:
        if db[MONGO_TABLE].insert(item):
            print('插入成功')
            return True
        return False

def main():
    get_first_json()

if __name__ == "__main__":
    main()

