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
	class Dog():
		def __init__(self,name):
			self.name=name
		def bulk(self):
			print("%s:My dog is wangwang!" % self.name)
		
	d1 = Dog("1").bulk()
	d2 = Dog("2").bulk()
	d3 = Dog("3").bulk()
	
	class cs():
		pass
		
	类实例化的时候可以增加和删除属性
	d1=Dog("1")
	d1.cc=True
	del d1.cc
	
	class people():
    age=12
    lst=[]
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def speak(self):
        print("English")
    def myForm(self):
        print('My name is:',self.name)

	class people():
		age=12
		lst=[]
		def __init__(self,name,sex):
			self.name=name
			self.sex=sex
		def speak(self):
			print("English")
		def myForm(self):
			print('My name is:',self.name)
		#默认找实例变量，找不到则会找类变量
		p1=people('chenlun','man')
		p1.age=13
		p1.high='175'
		p1.lst.append('test')
		print(p1.age,p1.lst,p1.high)
		del p1.high
		print(p1.age,p1.lst)
		p2=people('guojuan','wuman')
		print(p2.age,p2.lst)
	析构函数
		def __del__(self):
			pass
	私有方法，私有变量"__"
		__name
		def __age():
			pass
		
		
		
		
	