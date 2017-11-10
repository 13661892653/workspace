#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
myDict={'name':'colby'
    ,'sex':'man'
    ,'age':'18'
        }
ifexist=myDict.get('name')
print(ifexist)
if ifexist == None:
    myDict['name']='colby'
else:
    myDict['name'+'1']='colby2'
for k,v in myDict.items():
    print(k,v)