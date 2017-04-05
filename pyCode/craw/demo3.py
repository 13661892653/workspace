#coding=utf-8
#获取Cookie保存到变量
import http.cookiejar
import urllib
cookie = http.cookiejar.CookieJar()
#声明一个CookieJar对象实例来保存cookie
#利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
#此处的open方法同urllib的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name,':',item.value)
