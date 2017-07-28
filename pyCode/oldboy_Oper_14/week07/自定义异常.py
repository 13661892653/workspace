#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"

class ColbyException(Exception):
    def __init__(self,msg):
        self.msg=msg
    #def __str__(self):
    #    return
try:
    raise ColbyException('数据库链接异常！')
except Exception as e:
    print(e)
