#/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.5
#Tools :Pycharm 2017.01

def confirm(user,password):
    for i in open('userList.txt', 'r'):
        usr=i.split(',')[0]
        pwd=i.split(',')[1]
        flag = i.split(',')[2]
        print(usr,pwd,flag)
        if usr==user:
            if flag!='y':
                print("该用户已经锁定，系统退出！")
                break
            if pwd==password:
                return "登录成功！"
    else:
        print("不存在此用户，请检查用户名！")
if __name__=="__main__":
    for i in range(3):
        usr = input("登陆用户名：")
        pwd = input("登陆密码：")
        msg=confirm(usr,pwd)
        if msg=="登录成功！":
            print("登录成功！")
        break