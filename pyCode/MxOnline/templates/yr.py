#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm
__date__ = '2018/2/9 15:52'
__author__ = "Colby"

def yanzheng(fun):
    def addFun(arg1,arg2):
        print('one')
        print('two')
        print('three')
        return fun(arg1,arg2)
    return addFun

@yanzheng
def user(arg1,arg2):
    print('start....',arg1,arg2)

@yanzheng
def student(arg1,arg2):
    print('end....',arg1,arg2)

for i in range(1,10):
    print("=============%s==================" %i)
    user('colby','man')
    student('chen','男')