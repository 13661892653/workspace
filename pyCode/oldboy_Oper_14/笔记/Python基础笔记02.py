1、文件操作
	#读取文件
		f=open("yesterday",encoding="utf-8")#f就是内存对象
		data=f.read()
	#写入文件
		write("文件内容！")
		f.readlines 读取文件成为一个列表，每行作为一个元素
	#[读-写]文件
		f=open("yesterday","r+",encoding="utf-8")
	#[写-读]文件
		f=open("yesterday","w+",encoding="utf-8")
	#文件句柄，二进制文件rb/wb模式,以二进制编码，看到的不是0101010
		f=open("yesterday","rb")#不要指定encoding
		f=open("yesterday","wb")#不要指定encoding
		#字符串不转码是无法写入文件的
		f.write("hello binary\n".encode())
		f.close
	#打印文件指定行-适合小文件，比较low的写法
	for index,line in enumerate(f.readlines()):
		prin(line.strip())
		if index==9:
			print("----")
			continue
	#大文件操作	-比较high的高效的写法
		#迭代器、边读取边写入，缓冲区保留一行
		count=0
		for line in f:
			if count==9:
				print(line)
				count+=1
				continue
			print(line)
	#打印指针位置
		print(f.tell())#按字符计数
	#指针回到指定未知
		f.seek(0)#回到文件的初始位置
	#打印文件的编码
		print(f.encoding)
	#处理异常
		print(f.errors)
	#打印文件名称
		print(f.name)
	#判断光标是否可以移动
		print(f.seekable)
	#将缓冲区文件刷新到硬盘
		#f.flush()
		f.write("hello")#此处内容未写入文件
		f.flush()#已经刷入硬盘
	#打印进度条,flush缓存实时刷新
		import time,sys
		for i in range(100):
			sys.stdout.write("#")
			sys.stdout.flush()
			time.sleep(0.1)
	#快速清空文件truncate
		f.truncate()#清空所有文件，截断所有内容
		f.truncate(10)#从第10个字符开始截断
	
	#文件修改操作：
		f1=open("yesterday","r",encoding="utf-8")
		f2=open("yesterday","w",encoding="utf-8")
		for line in f1:
			if "ddd" in line:
				line=line.replace("ddd","ccc")
			f2.write(line)
	#系统参数替换,两个参数赋值
		str1=sys.argv[1]
		str2=sys.argv[2]
	#with语句操作文件,自动关闭文件
		with open('logfile','r') as f:
			for line in f:
				print(line)
	
2、字符编码与转码
	Unicode 万国码，显示全球各个国家的字符，每个字符均占位2个字节16bit
		为了解决浪费空间的问题出现了utf-8
		utf-8:所有英文字符占一个字节，所有中文占三个字节
	日本机器显示中文字符：
3、函数详解
**kwargs 接受N个关键字参数，转换成字典的方式传入
 *args	 接受N个位置参数，转换成元组的形式传入，无法接受关键字参数	
#函数跟过程的区别就是是否有返回值,过程就是没有返回值的函数
关键字参数不能写在位置参数前面。
def test1(x):
	'''函数描述，讲清楚函数是干什么的'''
	pass
位置参数、关键字参数、默认参数

			
def test3(name,*args,**kwargs):
	print(name)
	print(args)
	print(kwargs)
	
局部变量、全局变量：
	全局变量声明，global param	
	
递归函数：一个函数在内部自己调用自己
	#Python最大递归次数999
	特性：	1、必须有明确的结束条件
			2、每次进入更深一层递归时，问题规模应比上次递归都应有所减少
			3、效率比较低
	#自己调用自己，每次除以2
	def calc(n):
		print(n)
		return calc(n/2)
		
函数式编程：
	例子：函数嵌套函数:concat(left(right(n,2),2),2)

高阶函数:一个函数可以接受另一个函数作为自己的变量，那么这个函数就是高阶函数
	def add(a,b,f):
		return f(a)+f(b)
	res=add(3,-6,abs)
	print(res)

总结：集合，字典，文件操作，字符编码，函数式编程，局部变量、全局变量、递归、高阶函数作业
字符串转成字典：
b='''{'age':10}'''
eval(b)
	