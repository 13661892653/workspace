#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"

import urllib.request
from lxml import etree

def postData():
    data={
        'user':'13661892653',
        'pwd':'xlh123456789',
        'location':'http://crm.easyrong.com/data/keyindex'
    }
if __name__=="__main__":
    url='http://crm.easyrong.com'
    openurl=urllib.request.urlopen(url)
    html=openurl.read()
