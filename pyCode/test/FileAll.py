#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__date__ = '2018/1/2 15:57'
__author__ = "Colby"
import os
import sys
sys.setrecursionlimit(1000000)

def NotExist(filename):
    flag=False
    exceptList=['eot','ttf','woff']
    for i in exceptList:
        if i==filename:
            flag=True
    return flag

def WriteFile(filename):
    SourceFile = filename
    print('filename',filename)
    TargetFile = "C:\\Users\chenlun\Desktop\code.txt"
    t=open(TargetFile, 'a',encoding="utf-8")
    s=open(SourceFile,'r',encoding="utf-8")
    for line in s:
       t.write(line)
    t.write("\n\n")
    s.close()
    t.close()

def ScanDir(path):
    filename=os.walk(path)
    for i in filename:
        if len(i[2])==0:
            pass
        else:
            for j in i [2]:
                flag=NotExist(j.split('.')[1])
                if flag==False:
                    fileName=os.path.join(i[0],j)
                    WriteFile(fileName)

if __name__ == "__main__":
    Path = "C:\\Users\chenlun\Desktop\miniApp-master"
    ScanDir(Path)