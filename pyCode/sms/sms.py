#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from core.logIn import login
if __name__=='__main__':
    print(
        '''
        ***用户登录***
        '''
    )
    cnt=3
    while cnt<=3:
        user = input('input userName:')
        password = input('input password:')
        login(user,password)