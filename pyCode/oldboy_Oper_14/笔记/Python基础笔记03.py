������
������
��ҵ
ʵ��ATM�����̳ǵĳ���
Pythonװ������
	���壺�����Ǻ���������װ������������Ϊ����������Ӹ��ӹ���
	ԭ��1�������޸ı�װ�εĺ�����Դ����
	2�������޸ı�װ�εĺ����ĵ��÷�ʽ
ʵ��װ������֪ʶ����
1������������
2���߽׺���
3��Ƕ�׺���
�߽׺���+Ƕ�׺���-->װ����
Ƕ�׺���ʵ����
	x=0
	def grandpa():
		x=1
		def dad():
			x=2
			def son():
				x=3
				print(x)
			son()
		dad()
	grandpa()
	#���յ���������3
װ����ʵ����
example1:
	#coding=utf-8
	#Author:colby
	import time
	def timer(fun):#timer(test1)  func=test1
		def col(*args,**kwargs):
			print('in then col1')
			fun(*args,**kwargs)
			print('in then col2')
		return col
	@timer# test2 = timer(test2)  = deco  test2(name) =deco(name)
	def test1(name,age):
		time.sleep(1)
		print(name,age)
	test1('colby add new function!',30)
	���н����
		in then col1
		in the test1 colby add new function!
		in then col2
example2:
	import time
	user,passwd="colby","abc123"
	def auth(func):
		def wrapper(*args,**kwargs)
			username=input("Username:").strip()
			password=input("Password:").strip()
			if user==username and passwd=password:
				print("\033[32:1mUserhas passed authentication\033[0m")
				#�˴�����return�����������ؽ��
				#func(*args,**kwargs)
				return func(*args,**kwargs) 
			else:
				exit("\033[31:1mUserhas passed authentication\033[0m")
		return wrapper
	def index1():
		print("welcome to index page!")
	def index2():
		print("welcome to index page!")
	def index3():
		print("welcome to index page!")
	#��������
	@auth(auth_type="local")
	index1()
	@auth(auth_type="ldap")
	index2()
�б�����ʽ
	[i*2 for i in range(0,10)]
	�Ѿ����ɣ�ռ���ڴ�ռ�
��������generater	
	һ��(i*2 for i in range(0,10))
	�����㷨����ʵ�����ݣ���ռ���ڴ�ռ�
	�ܽ᣺1��ֻ���ڵ���ʱ�Ż�������Ӧ������
	2��ֻ��¼��ǰλ��
	3��ֻ��һ��__next__()������2.7��next()����
	������yield��������
������Iterator
	���ǿ�������forѭ���Ķ�����Iterable����
	���ǿ�������__next__()�������ǵ�����
	������һ���ǵ���������������һ����������
	list��dict��str��Iterator���ڵ�������ͨ��iter()����
	���Ա�ɵ�����
	range(10)��xrange(10)Ҳ�ǵ�����

	
	
	
	
	