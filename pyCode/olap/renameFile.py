#coding=utf-8
'''批量修改文件的名称，后缀加上"_程序猿"'''
import os
import shutil
initPath='F:\内部资料\数据挖掘学习视频'
list = os.listdir(initPath)
print(list)
for i in list:
    q=i.split('.')[0]
    h=i.split('.')[1]
    if h=='csf':
        q=q+'_程序员'
        filePath=os.path.join(initPath,i)
        newfilePath=os.path.join(initPath,q+'.csf')
        print(filePath)
        print(newfilePath)
        os.rename(filePath, newfilePath)