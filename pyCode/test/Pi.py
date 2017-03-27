#coding=utf-8
#抛出所有异常，提供相应提示信息
import re
try:
    cnt=10/0
    print(cnt)
except ZeroDivisionError as err:
    print("0不能作为被除数,请检查输入参数!",err)
class Myclass:
    i=12345
    def f(self):
        return "hello"
c=Myclass()
print(c.i)
