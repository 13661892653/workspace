#coding=utf-8
import re
import urllib.request
string="http://www.baidu.com"
pattr=re.compile(r"\w+://()*")
print(re.match(pattr,string).group())
print(dir(urllib.request.urlretrieve))