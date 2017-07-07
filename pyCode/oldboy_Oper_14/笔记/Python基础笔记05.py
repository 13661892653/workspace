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