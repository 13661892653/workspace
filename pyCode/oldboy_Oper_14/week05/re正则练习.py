#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"
'''
. 匹配除了换行之外的任意个字符
+ 1次或者多次
？ 匹配前面的字符0次或者1次
* 0次或者多次
match从字符串开头开始匹配
search从整个文本匹配，如果有多个，只匹配显示第一个
findall没有group()方法
'\'左斜杠转义
'''
import re
res=re.match('^colby\d+','colby123chenlun')
print(res.group())
#动态匹配省份日期格式
res=re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{8})","511303199704200240").groupdict()
print(res)

'''
re.split()用正则分割字符串
re.sub()
'''
print('split的用法:',re.split('[0-9]+','aa22bb55cc66'))
print('sub的用法:',re.sub('[0-9]+','|','aa22bb55cc66'))
print(re.search(r"a\\b","aa\\bb"))