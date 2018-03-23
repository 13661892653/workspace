#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
'''
本脚本主要功能：将微信手工保存的图片文件名称改成带日期的规范名称
'''
__author__ = "Colby"
import os,sys,time,datetime,re
def rm(dir,fileNameSource,fileNameTarget,houzui):
    '''
    执行更名操作
    :param dir: 
    :param fileNameSource: 
    :param fileNameTarget: 
    :param houzui: 
    :return: 
    '''
    fileNameSource=os.path.join(dir,fileNameSource+'.'+houzui)
    fileNameTarget=os.path.join(dir,fileNameTarget+'.'+houzui)
    try:
        os.rename(fileNameSource,fileNameTarget)
        print('已经修改成功')
    except FileExistsError as e:
        print(e.message)
def startFormatDate(fileName):
    '''
    日期格式化为yyyymmdd_hhMMSS
    :param fileName: 
    :return: 
    '''
    fileName_source=fileName
    fileName=time.strftime('%Y%m%d_%H%M%S', time.localtime(int(fileName)))
    print('文件%s已准备更名为：'%fileName_source,fileName)
    return fileName

def getImageName(dir):
    '''
    获取传入路径的文件名称
    :param dir: 
    :return: 
    '''
    fileList=os.listdir(dir)
    print('在目录%s扫描到如下文件:'%dir)
    for i in fileList:
        print('    '+i)
    for fileName in fileList:
        fileNameSource=fileName.split(".")
        fileNameSource_file = fileName.split(".")[0]
        fileNameSource_houzui = fileName.split(".")[1]
        res=re.compile(r'\d+')
        file1=str(res.search(str(fileNameSource_file)).group())
        print(file1)
        #截取左边10位
        file2=file1[0:10]
        if fileNameSource_houzui=='jpg' or fileNameSource_houzui=='jpeg':
            file3='IMG_'+startFormatDate(file2)
        elif fileNameSource_houzui=='mp4':
            file3=startFormatDate(file2)
        rm(dir,fileNameSource_file,file3,fileNameSource_houzui)
if __name__=="__main__":
    dir="F:\\BaiduNetdiskDownload\\WeiXin - 副本"
    getImageName(dir)
