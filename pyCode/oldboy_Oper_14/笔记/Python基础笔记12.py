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
	from sqlalchemy import create_engine
	from sqlalchemy.ext.declarative import declarative_base
	from sqlalchemy import Column,Integer,String
	from sqlalchemy.orm import sessionmaker
	from sqlalchemy import func
	engine=create_engine(
		"mysql+pymysql://root:root@localhost/ob",
		encoding='utf-8',echo=False
	)
	Base=declarative_base()#生成orm基类
	class User(Base):
		__tablename__='user'
		id=Column(Integer,primary_key=True)
		name=Column(String(32))
		password=Column(String(64))

		def __repr__(self):
			return '<%s,%s,%s>' %(self.id,self.name,self.password)
	Base.metadata.create_all(engine)
	Session_class=sessionmaker(bind=engine)#创建与数据库的会话class
	Session=Session_class()#生成session实例，跟cursor一样
	#增加数据
	#user_obj=User(name='colby',password='123456')#生成你要创建的数据对象
	#print(user_obj.name,user_obj.password)
	#Session.add(user_obj)#把要创建的数据对象，添加到这个session里
	#Session.commit()#统一提交，创建数据
	#查询数据
	#data=Session.query(User).filter_by(password='123456').filter_by(name='colby').first()#查询不需要commit
	#print(data)
	#修改数据
	#data.name='Guo'
	#data.password='Guo'
	Session.commit()
	#数据回滚
	Session.rollback()
	#filter(User.name.in_(['name1','name2']))
	#统计
	data=Session.query(User).filter_by(password='Guo').\
		filter_by(name='Guo').count()#查询不需要commit
	print(data)
	#分组
	data=Session.query(User.name,func.count(User.name)).group_by(User.name).all()
	print(data)
	
	
	
	
	
	