#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"
import hashlib
m=hashlib.md5()
m.update(b"hello")
print(m.hexdigest())

s=hashlib.sha512()
s.update(b"hello")
print(s.hexdigest())

import hmac
h=hmac.new(b'wueiqi',b'colby')
print(h.hexdigest())