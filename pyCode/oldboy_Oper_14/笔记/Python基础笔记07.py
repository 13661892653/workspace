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