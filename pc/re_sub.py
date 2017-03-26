#coding=utf-8
import re
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say,hello world,hello chenlun'
print(re.match(pattern,s).group())
print(re.sub(pattern,r'\2', s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
#print(re.sub(pattern,func, s))
### output ###
# say i, world hello!
# I Say, Hello World!
