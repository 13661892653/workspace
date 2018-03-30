#coding=utf-8
import re
s='1<a>b<a>cc<a>dd<a>gg'
res=re.compile('.*?(<a>).*?')
result=res.findall(s)
print('result',result)