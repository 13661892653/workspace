迭代器
生成器
作业
实现ATM购物商城的程序
Python装饰器：
	定义：本质是函数，用来装饰其他函数，为其他函数添加附加功能
	原则：1、不能修改被装饰的函数的源代码
	2、不能修改被装饰的函数的调用方式
实现装饰器的知识储备
1、函数即变量
2、高阶函数
3、嵌套函数
高阶函数+嵌套函数-->装饰器
嵌套函数实例：
	x=0
	def grandpa():
		x=1
		def dad():
			x=2
			def son():
				x=3
				print(x)
			son()
		dad()
	grandpa()
	#最终的输出结果是3
装饰器实例：
example1:
	#coding=utf-8
	#Author:colby
	import time
	def timer(fun):#timer(test1)  func=test1
		def col(*args,**kwargs):
			print('in then col1')
			fun(*args,**kwargs)
			print('in then col2')
		return col
	@timer# test2 = timer(test2)  = deco  test2(name) =deco(name)
	def test1(name,age):
		time.sleep(1)
		print(name,age)
	test1('colby add new function!',30)
	运行结果：
		in then col1
		in the test1 colby add new function!
		in then col2
example2:
	import time
	user,passwd="colby","abc123"
	def auth(func):
		def wrapper(*args,**kwargs)
			username=input("Username:").strip()
			password=input("Password:").strip()
			if user==username and passwd=password:
				print("\033[32:1mUserhas passed authentication\033[0m")
				#此处不加return，则函数不返回结果
				#func(*args,**kwargs)
				return func(*args,**kwargs) 
			else:
				exit("\033[31:1mUserhas passed authentication\033[0m")
		return wrapper
	def index1():
		print("welcome to index page!")
	def index2():
		print("welcome to index page!")
	def index3():
		print("welcome to index page!")
	#函数调用
	@auth(auth_type="local")
	index1()
	@auth(auth_type="ldap")
	index2()
列表生成式
	[i*2 for i in range(0,10)]
	已经生成，占用内存空间
生成器：generater	
	一、(i*2 for i in range(0,10))
	产生算法，无实际数据，不占用内存空间
	总结：1、只有在调用时才会生成相应的数据
	2、只记录当前位置
	3、只有一个__next__()方法，2.7是next()方法
	二、带yield的生成器
迭代器Iterator
	凡是可作用于for循环的对象都是Iterable类型
	凡是可作用于__next__()方法就是迭代器
	生成器一定是迭代器，迭代器不一定是生成器
	list、dict、str等Iterator属于迭代对象，通过iter()方法
	可以变成迭代器
	range(10)，xrange(10)也是迭代器

	
	
	
	
	