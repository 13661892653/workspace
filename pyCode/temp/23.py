#coding=utf-8
import os
def testFile():
    filename = input("请输入文件名：")
    if os.path.exists(filename):
        fp = open(filename, 'a')
    else:
        fp = open(filename, 'w')
    content=input("输入内容：")
    if content=='#':
        fp.close()
    else:
        fp.write(content+'\n')
        fp.close()

    f = open(filename, "r")
    content = f.read()
    print(content)

if __name__=="__main__":
    testFile()
