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
	import time
	def timer(fun):
		def col():
		    print('in the col1')
		    fun()
		    print('in the col2')
		return col
	
	@timer
	def test1():
	time.sleep(1)
	print("in the test1")
	test1()
	���н����
		in the col1
		in the test1
		in the col2
	