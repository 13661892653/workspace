#coding=utf-8
'''判断是否存在文件夹，不存在则创建对应的文件夹！'''
import os
import shutil
path='F:\pythonTest'
for i in range(1,1000000):
    print(path+'\\'+str(i))
    isExists = os.path.isdir(path+'\\'+str(i))
    print(isExists)
    if not isExists:
        print(isExists,'不存在！')
        os.mkdir(path+'\\'+str(i))
    else:
        print(isExists, '已经存在！')
    i+=1