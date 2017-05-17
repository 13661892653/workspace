#!/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
import os
import urllib.request
import time
from lxml import etree


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')

    '''代理服务器
    proxies=['120.90.6.92:8080','123.96.137.122:3128','175.155.25.13:808','58.59.155.97:8118','183.32.88.54:808','60.178.87.55:808','175.155.244.30:808','115.215.208.119:8118','121.61.86.225:808','175.23.37.45:80']
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)'''
    response = urllib.request.urlopen(url)
    html = response.read()
    return html
def get_page(url):
    html = url_open(url)
    print(html)
    a = html.find('current-comment-page') + 23
    print(a)
    b = html.find(']', a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    selector = etree.HTML(html)
    img_addrs = selector.xpath('//ol[@class="commentlist"]/li/div[1]/div/div[2]/p/a/@href')
    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        img = b'http:' + each
        filename = img.split('/')[-1]
        with open(filename, 'wb') as f:
            print(img)
            pic = url_open(img)
            print(pic)
            f.write(pic)


def download_mm(folder='OOXX'):
    #os.mkdir(folder)
    os.chdir(folder)
    url ="http://jandan.net/ooxx/"
    page_num = int(get_page(url))
    for i in range(page_num):
        print(page_num)
        print(i)
        page_url = url + 'page-' + str(i) + b'#comments'
        print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
    time.sleep(10)