#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__='colby'
import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='ob'
)
#cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor=conn.cursor()
cursor.execute("select id,gradename,ds from grade limit 10")
result=cursor.fetchmany(5)
#result=cursor.fetchall()
#result=cursor.fetchone()
num=1
for i in result:
    print('%s' % num,i)
    num+=1
conn.commit()
cursor.execute("insert into grade(id,gradename,ds) values(106,'num006','2017-08-15')")
conn.commit()
cursor.close()
conn.close()
#data=[
#		('001','name1')
#		('002','name2')
#	]
#	cursor.executemany('insert into student(id,name)
#	values(%s,%s)',data)