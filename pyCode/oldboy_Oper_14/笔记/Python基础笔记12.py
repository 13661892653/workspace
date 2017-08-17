Mysql-基本操作
	-略
Python操作Mysql
	#Python操作mysql基本语法
	#pip install pymysql
	import pymysql
	conn=pymysql.connect(
		host='主机名称或者IP地址',
		port=3306,
		user='userName',
		passwd='passwordName',
		db='dbname'
	)
	#cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
	cursor=conn.cursor()
	cursor.execute("select id,gradename,ds from grade limit 10")
	result=cursor.fetchmany(5)
	
	#批量插入数据
	data=[
		('001','name1')
		('002','name2')
	]
	cursor.executemany('insert into student(id,name) 
	values(%s,%s)',data)
	
ORM介绍(Object Relational Mapper)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	