#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__date__ = '2018/1/11 15:31'
__author__ = "Colby"
class A(object):
    def __init__(self):
        print('初始化A')

class B(object):
    def __new__(cls,age):
        print('第一步')
        print(object.__new__(B))
        return object.__new__(B)
    def __init__(self,age):
        print('第二步', self)
    def fun(self):
        print(self.age)
b=B(1)
