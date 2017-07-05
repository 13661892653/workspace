1、内置参数讲解
	all() any() 
	建议自己学习dir or type学习
	Python一切皆对象
pow(2,8)次方
round(1.234,2)四舍五入
zip拉链
	a=[1,2,3,4]
	b=[a,b,c,d]
	zip(a,b)
		(1,a)
		(2,b)
		(3,c)
		(4,d)
2、Json序列化,不同语言数据交互
	序列化与反序列化
	import json
	info={
		'name':colby,
		'age':20
	}
	#序列化
	f=open("test.txt",'w')
	f.write(json.dumps(info)
	#反序列化
	f=open("test.txt",'r')
	data=json.loads(f.read()
3、pickle同json，能处理复杂的数据类型	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	