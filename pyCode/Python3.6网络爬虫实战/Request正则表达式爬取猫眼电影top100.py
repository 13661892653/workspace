#coding=utf-8
import requests
from requests.exceptions import RequestException
import re
from  multiprocessing import Pool
import json
def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/24.0'}
    #print('requests.get',requests.get(url,headers=headers))
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #print('html',html)
    pattern=re.compile('<dd>.*?board-index-.*?">(\d+)</i>'
                        +'.*?data-src="(.*?)".*?/>.*?</a>'
                        +'.*?name"><a.*?title="(.*?)".*?>.*?</p>'
                        +'.*?<p.*?star">(.*?)</p>'
                        +'.*?<p.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>'
                        +'.*?fraction">(.*?)</i>.*?</dd>'
                        , re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            '排名': item[0],
            '首页图片': item[1],
            '电影名称': item[2].strip(),
            '主演': item[3].strip()[3:],
            '开播时间': item[4].strip()[5:],
            '评分': item[5]+item[6],
        }

def main(offset):
    url='http://maoyan.com/board/4?offset=%s' %(offset)
    html=get_one_page(url)
    items=parse_one_page(html)
    for item in items:
        print(item)
        write_to_file(item)

def write_to_file(content):
    with open('result.txt','a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
if __name__=="__main__":
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])
    # for i in range(10):
    #     main(i*10)