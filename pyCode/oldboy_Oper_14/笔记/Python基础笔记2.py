1���ļ�����
	#��ȡ�ļ�
		f=open("yesterday",encoding="utf-8")#f�����ڴ����
		data=f.read()
	#д���ļ�
		write("�ļ����ݣ�")
		f.readlines ��ȡ�ļ���Ϊһ���б�ÿ����Ϊһ��Ԫ��
	#[��-д]�ļ�
		f=open("yesterday","r+",encoding="utf-8")
	#[д-��]�ļ�
		f=open("yesterday","w+",encoding="utf-8")
	#�ļ�������������ļ�rb/wbģʽ,�Զ����Ʊ��룬�����Ĳ���0101010
		f=open("yesterday","rb")#��Ҫָ��encoding
		f=open("yesterday","wb")#��Ҫָ��encoding
		#�ַ�����ת�����޷�д���ļ���
		f.write("hello binary\n".encode())
		f.close
	#��ӡ�ļ�ָ����-�ʺ�С�ļ����Ƚ�low��д��
	for index,line in enumerate(f.readlines()):
		prin(line.strip())
		if index==9:
			print("----")
			continue
	#���ļ�����	-�Ƚ�high�ĸ�Ч��д��
		#���������߶�ȡ��д�룬����������һ��
		count=0
		for line in f:
			if count==9:
				print(line)
				count+=1
				continue
			print(line)
	#��ӡָ��λ��
		print(f.tell())#���ַ�����
	#ָ��ص�ָ��δ֪
		f.seek(0)#�ص��ļ��ĳ�ʼλ��
	#��ӡ�ļ��ı���
		print(f.encoding)
	#�����쳣
		print(f.errors)
	#��ӡ�ļ�����
		print(f.name)
	#�жϹ���Ƿ�����ƶ�
		print(f.seekable)
	#���������ļ�ˢ�µ�Ӳ��
		#f.flush()
		f.write("hello")#�˴�����δд���ļ�
		f.flush()#�Ѿ�ˢ��Ӳ��
	#��ӡ������,flush����ʵʱˢ��
		import time,sys
		for i in range(100):
			sys.stdout.write("#")
			sys.stdout.flush()
			time.sleep(0.1)
	#��������ļ�truncate
		f.truncate()#��������ļ����ض���������
		f.truncate(10)#�ӵ�10���ַ���ʼ�ض�
	
	#�ļ��޸Ĳ�����
		f1=open("yesterday","r",encoding="utf-8")
		f2=open("yesterday","w",encoding="utf-8")
		for line in f1:
			if "ddd" in line:
				line=line.replace("ddd","ccc")
			f2.write(line)
	#ϵͳ�����滻,����������ֵ
		str1=sys.argv[1]
		str2=sys.argv[2]
	#with�������ļ�,�Զ��ر��ļ�
		with open('logfile','r') as f:
			for line in f:
				print(line)
	
2���ַ�������ת��
	Unicode ����룬��ʾȫ��������ҵ��ַ���ÿ���ַ���ռλ2���ֽ�16bit
		Ϊ�˽���˷ѿռ�����������utf-8
		utf-8:����Ӣ���ַ�ռһ���ֽڣ���������ռ�����ֽ�
	�ձ�������ʾ�����ַ���
		
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	