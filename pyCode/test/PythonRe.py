#coding=utf-8
import re
s = '''first line
second line
third line'''
#匹配行首数字、字母、下划线中任意一个字符一次或者多次
#^
regex_start=re.compile("^\w+")
print(regex_start.findall(s))
#匹配行首数字、字母、下划线中任意一个字符一次或者多次(多行模式)
regex_start_m=re.compile("^\w+",re.M)
print(regex_start_m.findall(s))
#$
#匹配行尾数字、字母、下划线中任意一个字符一次或者多次
regex_end=re.compile("\w+$")
print(regex_end.findall(s))
#匹配行尾数字、字母、下划线中任意一个字符一次或者多次(多行模式)
regex_end_m=re.compile("\w+$",re.M)
print(regex_end_m.findall(s))
s1=re.compile('.+')
print(s1.findall(s))
s2=re.compile('.+',re.S)
print(s2.findall(s))
