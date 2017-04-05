#coding=utf-8
import re
#从开头开始匹配
string="Mynameis\dchenlun"
pattern=re.compile(r'Mynameis')
print(re.match(pattern,string).group())
#匹配首字符开头
pattern2=re.compile(r'world')
print(re.search(pattern2,'aa   world!!!!!!!').group())
#按数字分隔
pattern3 = re.compile(r'\d+')
print (re.split(pattern3,'one1two2three3four4five'))
#匹配所有并以列表格式输出
print (re.findall(pattern3,'one1two2three3four4five'))
#match/search/findall