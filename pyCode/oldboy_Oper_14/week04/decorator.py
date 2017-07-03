#coding=utf-8
#Author:colby
import time
def timer(fun):#timer(test1)  func=test1
    def col(*args,**kwargs):
        print('in then col1')
        fun(*args,**kwargs)
        print('in then col2')
    return col
@timer# test2 = timer(test2)  = deco  test2(name) =deco(name)
def test1(name,age):
    time.sleep(1)
    print(name,age)
test1('colby add new function!',30)