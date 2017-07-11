#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import re
__author__ = "Colby"
def calc(p1):
    res=p1+1
    if res>=5:
        return res
    else:
        pass
    calc(res)
aa=calc(1)
print(aa)