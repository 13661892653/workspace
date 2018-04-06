#coding = utf-8
#Version:Python-3.6.0
__date__ = '2018/3/30 22:49'
__author__ = 'colby'
import requests
from pyquery import PyQuery
import pymongo
from requests.exceptions import ConnectionError
from urllib.parse import urlencode
base_url='http://weixin.sogou.com/weixin?'
headers={
    'Cookie': 'CXID=609A7E3D50D61D32DE21DA8042B9C206; SUID=DB0AC0B75C68860A5A9D47E800098D64; IPLOC=CN3100; ld=Wkllllllll2zHfgGlllllV$TItZlllllHDl3LZllll9lllllpylll5@@@@@@@@@@; SUV=005D6320B7C00ADB5AB7A5CDFFB69241; LSTMV=223%2C444; LCLKINT=3144; ad=MWIFRlllll2zXUKolllllV$TIN9lllllHDl3LZllll9lllllpylll5@@@@@@@@@@; ABTEST=0|1522486283|v1; weixinIndexVisited=1; SNUID=893580F73F3A5639589BDA884016B09A; sct=1; JSESSIONID=aaaqoD43M33RMfVu35Oiw; ppinf=5|1522851151|1524060751|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklOTklODglRTQlQkMlQTZ8Y3J0OjEwOjE1MjI4NTExNTF8cmVmbmljazoxODolRTklOTklODglRTQlQkMlQTZ8dXNlcmlkOjQ0Om85dDJsdUVFa1B3ZERYWU5BYnEtWGJ5bUU5UVFAd2VpeGluLnNvaHUuY29tfA; pprdig=ckSSTdS3cPxjxOXO9wiEEPbKKQlJKIOZA_nkVcMKF90hin3SfyJV_cjg3VMP9dxroDb9vFso-GUYn0sWF94Dtqs9jX0DJPkEzdnxNcVlF0K8nwdqv2DNIZM4Un358eFp94KfXiujRkOAnPXtPGQbzTrnevJ2tX52Ec3mBYh-TW4; sgid=10-34382973-AVrE3U8fIswDFPEsKwYKzSA; ppmdig=152285115100000067645c51c363b12b6a1f8a3cc70ebdbc',
    'Host': 'weixin.sogou.com',
    'Referer': 'http://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&_sug_type_=&sut=2333&lkt=1%2C1522812774360%2C1522812774360&s_from=input&_sug_=y&type=2&sst0=1522812774462&page=12&ie=utf8&w=01019900&dr=1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
}
proxy = None
max_count=5
count=0
def get_html(url,count=1):
    global proxy
    if count == max_count:
        print('重试次数太多了')
        return None
    try:
        if proxy:
            proxies={
                'http':'http://' + proxy
            }
            response=requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print('Response status:302')
            proxy = get_proxy()
            if proxy:
                print('正在使用代理：',proxy)
                return get_html(url)
            else:
                print('代理获取失败...')
                return None
    except ConnectionError:
        proxy=get_proxy()
        count+=1
        return get_html(url,count)

def get_proxy():
    try:
        proxy_pool_url='http://127.0.0.1:5555/random'
        response=requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return  None
    except ConnectionError:
        return None
def get_index(keyword,page):
    data = {
        'query': '风景',
        'type': 2,
        'page': '14'
    }
    url=base_url+urlencode(data)
    html=get_html(url)
    return html

def parse_index(html):
    doc=PyQuery(html)
    items=doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def main():
    for page in range(1,100):
        html=get_index('风景',page)
        if html:
            article_urls=parse_index(html)
            for article_url in article_urls:
                print('article_url',article_url)

if __name__  == "__main__":
    main()