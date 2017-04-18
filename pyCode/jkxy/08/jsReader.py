#coding=utf-8
import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
jscontent=requests.get('http://coral.qq.com/article/1165021596/comment?commentid=0&reqnum=100'
                       ,headers=headers).content.decode('utf-8')
print(jscontent)
jsDict=json.loads(jscontent)
jsData=jsDict['data']
comments=jsData['commentid']
for each in comments:
    print(each['content'])