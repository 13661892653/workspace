#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"

class Dog:
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print("%s:My dog is wangwang!" % self.name)

d2 = Dog("2")
d1 = Dog("1")

d3 = Dog("3")
print(d1)
print(d2)
print(d3)
