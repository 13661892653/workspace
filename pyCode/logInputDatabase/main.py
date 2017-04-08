#coding=utf-8
#!/usr/bin/python
import os
import re
import shutil

from mysqldb import *
#扫描文件夹，判断当天的文件是否上传到服务器
'''
CREATE TABLE tomcat
(
ds varchar(10) comment  '日志产生日期',
ds_time varchar(10) comment  '日志产生时间',
url varchar(1024) comment  '时间url',
event_id int comment  '时间id',
event_name varchar(255) comment  '事件名称',
member_id int comment  '用户id',
member_name varchar(255) comment  '用户名称',
primary key (member_id,event_id,ds,ds_time)
);
'''
def strRep(str):
    '''替换掉[]和换行符'''
    return str.replace('[','').replace(']','').replace('\n','')
def logAnalysis(line):
    reg = r'.*?INFO  EMBED - (.*?.+)'
    data = re.compile(reg)
    '''将列表转换成字符串，因为列表就一个元素'''
    dataList = strRep(re.findall(reg,line,re.DOTALL)[0])
    '''按空格分列'''
    return dataList.split(' ')

def loaddata(sql,data):
    '''批量加载数据入库'''
    connMysql = connDB()
    result=exeBath(connMysql[0], connMysql[1], sql,data)
    print('加载记录数:',result)
    connClose(connMysql[0], connMysql[1])

def deldata(sql):
    '''批量加载数据入库'''
    connMysql = connDB()
    result=exeUpdate(connMysql[0], connMysql[1], sql)
    print(sql,"执行完毕！")
    connClose(connMysql[0], connMysql[1])

def defineSql(type):
    if type=="D":
        sql="truncate table tomcat"
    if type == "I":
        sql="insert into tomcat(ds,ds_time,url,event_id,event_name,member_id,member_name) " \
            "values(%s,%s,%s,%s,%s,%s,%s)"
    return sql
#读取文件
def loginput(inputPath,outputPath,cntCommit):
    fileList = scan_files(inputPath)
    #清空表的所有数据据
    sqlD = defineSql("D")
    deldata(sqlD)
    for file in fileList:
        dataList = []
        i=0
        '''计算每个文件行数'''
        myfile = open(file,'r',encoding='gbk')
        lines = len(myfile.readlines())
        print('文件记录数：',lines)
        myfile.close()
        print("正在加载文件：",file)
        for line in open(file,'r',encoding='gbk'):
            #解析日志
            print(line)
            i += 1
            data=logAnalysis(line)
            dataList.append(tuple(data))
            '''数组长度等于设定的commit时，提交数据'''
            if len(dataList)==cntCommit:
                sqlI = defineSql("I")
                loaddata(sqlI, dataList)
                dataList=[]
            '''行数/commit行数余下行数的提交'''
            if lines==i:
                sqlI = defineSql("I")
                loaddata(sqlI, dataList)
        print("文件加载完毕：", file)
        moveFile(file, outputPath)
        print(file,'已经移到到：',outputPath)
'''读取完毕后将文件copy到outputFile'''
def moveFile(file,outputPath):
    #shutil.move(file, outputPath)
    pass

def scan_files(directory, prefix=None, postfix=None):
    '''扫描inputFile文件夹所有文件进行加载'''
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))
    return files_list
#退出程序

if __name__=="__main__":
    print("解析日志开始...")
    '''一次提交多少行，默认100行commit一次'''
    cntCommit=100
    currentPath=os.getcwd()
    inputPath=os.path.join(currentPath,'inputFile')
    outputPath=os.path.join(currentPath,'outputFile')
    loginput(inputPath,outputPath,cntCommit)