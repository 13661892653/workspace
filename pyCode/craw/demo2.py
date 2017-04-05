#coding=utf-8
"""网页抓取异常捕获"""
import urllib.request
#给了一个错误的网址
req=urllib.request.Request("http://nnn.baidu.com")
try:
    response = urllib.request.urlopen(req)
except urllib.request.URLError as e:
    print(e.reason)
"""错误原因是 getaddrinfo failed"""

req1 = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urllib.request.urlopen(req1)
except urllib.request.HTTPError as e:
    if hasattr(e,"code"):
        print("错误码",e.code)
    if hasattr(e,"reason"):
        print("错误原因",e.reason)
