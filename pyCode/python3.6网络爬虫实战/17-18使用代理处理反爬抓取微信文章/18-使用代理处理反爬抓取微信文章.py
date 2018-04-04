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
    'Cookie': 'CXID=283D9D19E87580EED7F466C0BC1C5E8D; SUV=00E039A2704091E259E475A43DFDB102; dt_ssuid=5496609390; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ssuid=6966476546; IPLOC=CN3100; pgv_pvi=8851393024; usid=bG9x1sdFmAjaoTRo; SUID=E29140704C238B0A59DC75970000FEC7; LSTMV=238%2C154; LCLKINT=2077; ad=kAs1tZllll2zgsDElllllV$sksolllllt9jSckllll9lllll9fgOls@@@@@@@@@@; ABTEST=4|1522810808|v1; weixinIndexVisited=1; sct=2; JSESSIONID=aaai0cYopdLkw54foLOiw; ppinf=5|1522816761|1524026361|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklOTklODglRTQlQkMlQTZ8Y3J0OjEwOjE1MjI4MTY3NjF8cmVmbmljazoxODolRTklOTklODglRTQlQkMlQTZ8dXNlcmlkOjQ0Om85dDJsdUVFa1B3ZERYWU5BYnEtWGJ5bUU5UVFAd2VpeGluLnNvaHUuY29tfA; pprdig=s8ruMuGlB2NXDSaU_napMl1svJ4wa3EOI34bMCfIr_S0YEPb7vNhMoTVkh1w-4Croeg7ohwBuG_cbf1TV-WtNQ3TiU62XQfUFIJkhscOF7cX4zVBj_pNSdBtxwXDpzCcRzg0goGTIBsREgh9-RzFbzC_dGqdCvYh99Huh9mJn4o; sgid=10-34382973-AVrEVvkA3sIt1yqmgC5Ue7s; PHPSESSID=qota29gvmqe1i12i0rbnrtme12; SUIR=495338504A4F22B74E0CA9354BF3F0B8; ppmdig=152283233400000003b3c5536c8c18305d2a8161e4f85ce1; seccodeErrorCount=1|Wed, 04 Apr 2018 09:36:53 GMT; SNUID=011A701803066A0182A7933F0336BFD4; seccodeRight=success; successCount=1|Wed, 04 Apr 2018 09:37:03 GMT',
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