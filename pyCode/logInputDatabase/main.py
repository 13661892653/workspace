#coding=utf-8
import os
import re
#扫描文件夹，判断当天的文件是否上传到服务器

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

#读取文件
def loginput(inputPath,outputPath,cntCommit):
    fileList = scan_files(inputPath)
    for file in fileList:
        dataList = []
        for line in open(file):
            #解析日志
            data=logAnalysis(line)
            dataList.append(tuple(data))
            print(dataList)
            #if lineNum=cntCommit


'''读取完毕后将文件copy到outputFile'''
def copyfile():
    pass

def scan_files(directory, prefix=None, postfix=None):
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