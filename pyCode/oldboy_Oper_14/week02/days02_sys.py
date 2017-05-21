#!/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
'''
import sys

print(sys.path)  # 打印环境变量
print(sys.argv)  # 打印脚本相对路径
#print(sys.argv[2])  # 获取用户传入的第三个参数

import os

os.system("dir")  # 执行命令不保存结果
print(os.popen("dir").read())  # 执行命令后可以保存结果
#os.mkdir("test_dir")  # 创建目录
'''
name=['bb','bb','cc','dd']
print(name.index('bb'))