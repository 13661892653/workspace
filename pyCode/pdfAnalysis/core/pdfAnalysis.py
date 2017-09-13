#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import xlrd
wb=xlrd.open_workbook('../data/嘉兴市洪合旺盛漂染有限公司_利润表.xls')
wb.sheet_names()
sh=wb.sheet_by_index(0)
sh=wb.sheet_by_name(u'Sheet1')
cnt=1
for rownum in range(sh.nrows):
    name=(sh.row_values(rownum)[0]).strip()
    amt=sh.row_values(rownum)[2]
    if name=='':
        pass
    else:
        if amt=='':
            amt=0
        print(cnt,name,amt)
        cnt+=1
