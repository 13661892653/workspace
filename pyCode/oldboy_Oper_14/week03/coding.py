#!/usr/bin/python
#coding=gbk
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3,[3,2,1])
f(3)
