Mysql-基本操作
	-略
Python操作Mysql
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
