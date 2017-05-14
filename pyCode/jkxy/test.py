#coding=utf-8
import re
s='''sdfxxhello
xxfsdfxxworldxxasdf'''
d=re.findall('xx(.*?)xx',s,re.S)
print(d)