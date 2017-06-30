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
	import time
	def timer(fun):
		def col():
		    print('in the col1')
		    fun()
		    print('in the col2')
		return col
	
	@timer
	def test1():
	time.sleep(1)
	print("in the test1")
	test1()
	运行结果：
		in the col1
		in the test1
		in the col2
	