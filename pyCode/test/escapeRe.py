#coding=utf-8
import re
s=".+\d123"
regex_str=re.escape(".+\d123")
print(regex_str)
print(re.findall(regex_str,s))

s = "the sum of 7 and 20 is [7+20]."
print(re.sub('\[7\+20\]', '27', s))
