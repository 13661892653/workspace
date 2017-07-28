静态方法
	@staticmethod#实际上跟类没什么关系了、名义上归所属类管理
	def eat(self):
		pass
类方法
	@classmethod#类方法只能访问类变量，不能访问实例变量
	def eat(self):
		pass
属性方法
	@property#把方法变成一个属性，eat()这样调用报错
	#属性方法无法删除 del d.eat()报错。正常情况是能正常删除的
	def eat(self):
		pass

类的特殊成员方法
__doc__，查看类描述或者注释的方法
__module__，输出当前类是从哪个模块导入的
__class__，输出当前类的类名
__call__对象后面加括号，触发执行
	注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
	class Foo: 
		def __init__(self):
			pass    
		def __call__(self, *args, **kwargs):
	 
			print '__call__'
 
	obj = Foo() # 执行 __init__
	obj()       # 执行 __call__
__dict__ 查看类或对象中的所有成员 
	class Province:
		country = 'China'
		def __init__(self, name, count):
			self.name = name
			self.count = count	 
		def func(self, *args, **kwargs):
			print 'func'
	# 获取类的成员，即：静态字段、方法、
	print Province.__dict__
	# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}
	obj1 = Province('HeBei',10000)
	print obj1.__dict__
	# 获取 对象obj1 的成员
	# 输出：{'count': 10000, 'name': 'HeBei'}	
	类调用返回类的方法，实例调用返回实例属性和变量	
__str__
	如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值
	class Foo:
		def __str__(self):
			return 'alex li'
	obj = Foo()
	print obj
	# 输出：alex li	
__getitem__、__setitem__、__delitem__		
	用于索引操作，如字典。以上分别表示获取、设置、删除数据	
		
__new__ \ __metaclass__
	
反射
	通过字符串映射或修改程序运行时的
	状态、属性、方法, 有以下4个方法	
	hasattr(obj,name_str) 判断一个对象里是否有对应字符串的方法
	getattr	根据字符串去获取obj对象里的对应的方法的内存地址
	setattr 设置新的属性
	delattr 删除用户自定义输入字符串对应的属性
	class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating..."%self.name,food)

	d = Dog("NiuHanYang")
	choice = input(">>:").strip()
	
	#判断用户输入的字符串是否为实例的属性或者方法
	if hasattr(d,choice):
		getattr(d,choice)
	else:
		setattr(d,choice,bulk) #d.talk = bulk
		func = getattr(d, choice)
		func(d)
	# #### 检查是否含有成员 ####
	hasattr(obj, 'name')
	hasattr(obj, 'func')
	 
	# #### 获取成员 ####
	getattr(obj, 'name')
	getattr(obj, 'func')
	 
	# #### 设置成员，为对象添加新的属性####
	setattr(obj, 'age', 18)
	setattr(obj, 'show', lambda num: num + 1)
	 
	# #### 删除成员 ####
	delattr(obj, 'name')
	delattr(obj, 'func')	
异常处理
	try:
		data['name']
	except KeyError as e :
		print("没有这个Key",e)
	except IndexError as e :
		print("列表操作错误",e)
	except Exception as e:
		print("未知错误")
	else:
		print("一切正常执行这个")
	finally：
		print("不管有错没错都执行的！")
	#不建议使用以下方法
	try:
		data['name']
	except (KeyError,IndexError) as e :
		print("没有这个Key",e)
	
自定义异常
	class ColbyException(Exception):
    def __init__(self,msg):
        self.msg=msg
    #def __str__(self):
    #    return
	try:
		raise ColbyException('数据库链接异常！')
	except Exception as e:
		print(e)


Socket网络编程
	OSI七层模型
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	