#/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
def lock(user):
    '''
    密码输错三次，锁定用户
    :param user: 
    :return: 
    '''
    data=[]
    file = open("userList.txt", "r+")
    readlines=file.readlines()
    print('readlines',readlines)
    for lines in readlines:
        if lines.split(',')[0]==user:
            lines=lines.split(',')[0]+','+lines.split(',')[1]+','+'n\n'
            print('lines:',lines)
        data.append(lines)
    print('data',data)
    file.close()
    output = open('userList.txt', 'w')
    output.writelines(data)
    output.close()
def confirm(user,password):
    '''
    验证用户密码的有效性
    :param user: 
    :param password: 
    :return: 
    '''
    for i in open('userList.txt', 'r'):
        usr=i.split(',')[0]
        pwd=i.split(',')[1]
        flag = i.split(',')[2]
        if usr==user:
            if flag!='y':
                return 2
            if pwd==password:
                return 1
            else:
                return -1
    else:
        return 0
if __name__=="__main__":
    notfund=0
    errfund=0
    for i in range(3):
        usr = input("登陆用户名：")
        pwd = input("登陆密码：")
        msg=confirm(usr,pwd)
        if msg==1:
            print("登录成功！")
            break
        if msg==2:
            print("该用户已经被锁定！")
            break
        elif msg==0:
            print("不存在此用户，请检查用户名！")
            notfund+=1
        elif msg == -1:
            errfund += 1
            print("密码错误",errfund,"次,3次将被锁定！")
            if errfund==3:
                lock(usr)
                print("密码错误3次，用户已被锁定，请联系管理员！")
    print('已经退出！')