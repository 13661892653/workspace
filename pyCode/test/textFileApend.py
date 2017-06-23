#/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
# os.walk()的使用
import os


# 枚举dirPath目录下的所有文件

def main(dir):
    # begin
    fileDir = dir  # 查找F:\aaa 目录下
    for a in os.walk(fileDir):
        # begin
        print(a[2])
    return a[2]
if __name__ == '__main__':
    # begin
    dir = 'F:\\视频\程序猿视频教程\\014-Linux运维视频零基础到精通大师shell ngix redis mysql nosql openstack 集群\\课程介绍'
    fileList=main(dir)
    print(fileList)
    f1=open("new.txt",'w')
    for i in fileList:
        path=os.path.join(dir,i)
        print(path)
        file=open(path,'r')
        f=file.readlines()
        for k in f:
            f1.write(k)
        f1.write('\n')

# end

#f2=open("F:\\视频\程序猿视频教程\\014-Linux运维视频零基础到精通大师shell ngix redis mysql nosql openstack 集群\\课程介绍\\new.txt","w")