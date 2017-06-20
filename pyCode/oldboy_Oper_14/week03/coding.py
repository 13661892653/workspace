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
def test1(*args,**kargs):
    pass
class test2():
    def self(x,y):
        self.x = x
        self.y = y
    def function(self):
        print(self.x)
        print(self.y)