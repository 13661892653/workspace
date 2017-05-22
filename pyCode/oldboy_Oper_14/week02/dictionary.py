#!/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
#对比findall与search的区别
import re
S2='asdfxxIxxlovexxdfd'
f2 = re.findall('xx(.*?)xx(.*?)xx',S2)
print(f2)