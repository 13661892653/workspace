内容提要
	面向对象的介绍
		特性：
			class
			object
			实例
			封装
			继承
			多态
		语法：
			属性
			方法
			构造函数
			析构函数
		私有方法，私有属性
		类变量
		实例变量
面向对象编程
	Encapsulation封装
	Inheritance继承
	Polymorphism多态
	class Dog:
		def __init__(self,name):
			self.name=name
		def bulk(self):
			print("%s:My dog is wangwang!" % self.name)
		
	d1 = Dog("1").bulk()
	d2 = Dog("2").bulk()
	d3 = Dog("3").bulk()
	
	class cs():
		pass