#coding=utf-8
with open('data.csv',encoding='utf-8') as file:
    for i in file:
        print(i.replace('\ufeff','').replace('\n','').split(','))