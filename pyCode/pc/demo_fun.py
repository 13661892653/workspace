#coding=utf-8
import re
#分组的应用
email=r'\w*@\w+(\.com|\.net)'
string='chenlun0420@126.com'
print(re.findall(email,string))
print(re.match(email,string).groups())
