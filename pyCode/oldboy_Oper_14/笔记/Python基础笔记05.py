1、常用模块的学习
模块的本质实现一块功能
包：本质就是一个目录，必须带有一个叫__init__.py的文件
导入模块：
import xx
	本质将xx代码执行了一遍，并且赋值给变量
	通过前缀调用变量和方法，运行xx.log()
from xx import logger
	本质将xx中某一部分的代码执行了一遍
	运行log()即可，无需加上模块前缀名
from xx import logger1,logger2 多个导入逗号分隔
from xx import logger as log
from xx import * 慎用，可能覆盖当前函数或者方法

导入包：
	本质是导入包下面的__init_.py文件

模块分类
	标准库
	开源模块
	自定义模块
	
标准库：
	datetime与time
		时间有三种格式：时间戳、元组，格式化的字符串
		time与datetime模块
		time.time()#时间戳
		time.localtime()#元组
		time.timezone()#时区
		time.gmtime()
			#传入秒返回，不传返回UTC时间
		time.strftime('%Y-%m-%d %H:%M:%S','')
		datetime是基于time的高级封装
			datetime.datetime.now()+datetime.timedelta(3)当前时间加3天
	random()
		chr()#将数字转换成字母
	os模块
	sys模块
		sys.argv：读取脚本后面的参数
		python test.py 1 2 3 4
			sys.argv获取后面的参数
		
	shutil模块
		高级的文件、文件夹、压缩包处理模块
		
	
	
	
	
	
	
	
	