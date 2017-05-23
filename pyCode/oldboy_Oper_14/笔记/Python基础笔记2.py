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
		
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	