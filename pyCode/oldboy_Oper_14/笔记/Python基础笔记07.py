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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	