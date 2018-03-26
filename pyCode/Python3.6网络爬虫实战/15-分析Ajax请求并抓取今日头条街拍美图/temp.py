#coding=utf-8
import requests
headers={
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
url='http://toutiao.com/group/6498650526673011214/'
html=requests.get(url,headers=headers)
print(html.content)
print(html.text)