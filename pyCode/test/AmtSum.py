#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import csv
import time
startTime='08'
endTime='12'
def timeDiff(startTime,hour,endTime):
    if startTime<=hour and hour<=endTime:
        return True
    else:
        return False

TotalAmt=0
with open('sale_record.csv') as f:
    reader=csv.DictReader(f)
    for row in reader:
        #取出时间
        currentTime=row['take_time'].split(' ')[1]
        # 取出小时
        hour=currentTime.split(':')[0]
        result=timeDiff(startTime,hour,endTime)
        if result:
            TotalAmt=int(row['sale_moeny'])+TotalAmt
print('总金额：',TotalAmt)