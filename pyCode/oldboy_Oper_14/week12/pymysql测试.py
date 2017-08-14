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
    db='world'
)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select * from city limit 10")
result=cursor.fetchall()
print(result)
for i in result:
    print(i)
conn.commit()
cursor.close()
conn.close()
new_id = cursor.lastrowid
print('new_id%s' %new_id)