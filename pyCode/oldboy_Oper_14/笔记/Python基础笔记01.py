课堂笔记
	标准库无需安装，直接import就可用的库，Python自带
	第三方库，需要下载并且安装才能使用
模块初识
	1、sys模块
		import sys
		print(sys.path)#打印环境变量
		导入模块时，先在当前目录进行查找，再到site-package查找，
		再去全局环境变量查找，如果都没有导入的模块名称，则报错
		print(sys.argv)#打印脚本相对路径
		print(sys.argv[2])#获取用户传入的第三个参数
		
	2、os模块
		import os
		os.system("dir")#执行命令不保存结果
		cmd_res=os.popen("dir").read()#执行命令后可以保存结果
		os.mkdir("test_dir")#创建目录
	3、.pyc是个什么东东
		Python是一门先编译后解释的语言，执行时先查找pyc文件，存在直接调用，
		不存在则将编译结果保存到内存中，程序运行结束后，保存到pyc文件中
	4、数据类型
		4-1数字
			整型、长整型、浮点型、complex复数
			长整型:Python的长整型没有指定位宽，但也不是无限大
			科学计数法:50000=5E4=5*10**4
		4-2布尔值
			1或者0
			True或者False
		4-3字符串
		4-4bytes数据类型
			编码转换(string<-->bytes)
			encode('utf-8')编码成2进制，编码之前为utf-8
			decode('utf-8')用utf-8解码
			for example:
				编码：'aa'.encode('utf-8')
					b'\xe2\....'
				解码：b'\xe2\....'.decode('utf-8')
					'aa'
	5、三元运算符
	6、进制
		16进制表示方法，后缀H或者前缀ox
	7、列表
		name=['aa','bb','cc','dd']
		name[-2:]#从倒数第二个取出所有
		name[:2]#从第一个取到下标为2所有元素
		增加
			name.append("ee") #追加
			name.insert(2,"ff") #将ff插入到下标为1的后面
		修改
			name[2]='gg'
		删除
			name.remove('gg')#直接删除指定元素
			del name[1]#按下标删除
			name.pop()#不指定参数弹出最后一个
			name.pop(1)#弹出下标为1的元素
		查找元素位置
			name.index('aa')
		清空列表
			name.clear()
		排序
			name.sort()#默认ASCII排序
			name.extend(列表)#合并列表
		import copy
			浅copy(copy内存地址)与深copy(完全独立copy一份)
			copy.copy()与copy.deepcopy()
		列表循环
			for i in list:
				print(i)
		步长切片		
			print(name[0:-1:2])#跳着切片，步长2
		
	8、元组
		list=['a','b','c']
		for i in enumerate(list):
			print(i)
		#打印列表和下标值
			(0,a)
			(1,b)
			(2,c)
	9、字符串
		name='colby'
		name.capitalize#首字母大写
			>>Colby
		name.center(50,'-')#打印50个字符，长度不够两端用'-'补齐
		name.ljust(50,'-')#打印50个字符，长度不够左边用'-'补齐
		name.rjust(50,'-')#打印50个字符，长度不够右边用'-'补齐
			>>---colby---
		name.endwith('by')#判断字符以什么结尾
			>>True
		name.expand()#tab键转成多少个字符
		name.find('y')#返回字符所在索引
			>>4
		name.rfind('c')#找到最右边的指定字符
		>>name='colby{name},{age}'
			name.format(name='colby',age=22)
			name.format_map({'name':'colby','age':22})
			传入的值会默认带到name变量中去
		name.isalnum()#判断是否为阿拉伯数字和字符
		name.isalpha()#判断是否为纯英文字符
		name.isdecimal()#判断是十进制
		name.isdigit()#判断是否为整数
		name.isidentifier()#判断是否是一个合法的标识符变量
		name.islower()#判断是否为小写
		name.isupper()#判断是否为大写
		name.isnumeric()#判断是否为整数
		join的用法
			print(','.join(['a','b','c'])
			>>a,b,c  #将列表转成字符，以逗号分隔
		name.lower()#转成小写
		name.upper()#转成大写
		name.strip()#去掉两端换行符
		name.lstrip()#去掉左边换行符
		name.rstrip()#去掉右边换行符
		随机密码-加密解密(可以给一串乱七八糟的字符用于加密)
		p=str.maketrans('abcdefg','1234567')#将abcdefg映射成1234567
			print('colby'.translate(p)
			>>3ol2y
		name.replace('c','C')#字符串替换
		name.split(',')#字符串按照指定字符分隔成列表
		name.splitlines()#按换行符分隔，Linux与windows方法一样
		name.swapcase()#大小写互换
		name.title()#驼峰
		name.zfill()#用0补齐
	10、字典
		增加
			info['age']=10
		删除
			del info.get("name")#安全删除
		修改
			info['age']=10
		查找
			info.get("name")#存在返回，不存在为None
			info['name']
		合并更新
			b={'name':'colby','age':'29','height':'75Kg'}
			info.update()#存在就更新，不存在就新增
		info.values()#打印所有值
		info.keys()#打印所键
		info.setdefault('name','age')#存在就显示，不存在就新增一个值
		多级字典嵌套操作
			info['person']['age'][1]=90
		info.item()#将字段转成列表
		initDict=dict.fromkeys([6,7,8],[1,{"name":"colby"},444])
			#字典初始化
			#值引用的同一个内存地址，注意，修改一个等于修改All
		字典的循环
			#高效的写法，建议使用
			for i in info:
				print(i,info[i])
			#效率低，不建议使用
			for k,v in info.items():
				print(k,v)
	11、集合set
		交集 & intersection 返回集合
		并集 | union 返回集合
		差集 - difference 返回集合
		对称差集 ^ symmetric_difference 不同时存在两个集合中
		子集issubset True或者False
		父集isupperset True或者False
		集合添加一个元素 add
		集合添加多个元素 update
		集合删除元素 remove
			字符串、列表、字典、集合判断字符是否存在里边
			for in str/list/set/dict:
				print(i)
		
			
			
			
			
			
		