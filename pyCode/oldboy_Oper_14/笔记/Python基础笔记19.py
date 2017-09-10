上节内容回顾：
	1、Django请求生命周期
		-> URL对应关系（匹配） -> 视图函数 -> 返回用户字符串
		-> URL对应关系（匹配） -> 视图函数 -> 打开一个HTML文件，读取内容
		
	2、创建django projcet

		django-admin startproject mysite
		

		..
		
		mysite
			mysite
				- 配置文件
				- url.py
				- settings.py
			
		cd mysite
		python manage.py startapp cmdb
		
		mysite
			mysite
				- 配置文件
				- url.py
				- settings.py
			cmdb
				- views.py
				- admin.py
				- models.py # 创建数据库表

	3、配置
		
		模板路径
		静态文件路径
		# CSRF
		
	4、编写程序

		a. url.py
			
			/index/    ->   func
			
		b. views.py
			
			def func(request):
				# 包含所有的请求数据
				...
				return HttpResponse('字符串')
				return render(request, 'index.html', {''})
				retrun redirect('URL')
				
		c. 模板语言
			return render(request, 'index.html', {'li': [11,22,33]})
			
			{% for item in li %}
				<h1>{{item}}</h1>
			{% endfor %}
			
			
			***********  索引用点 **********
			<h2> {{item.0 }} </h2>

一、路由系统，URL
	1、url(r'^index/', views.index),    
		url(r'^home/', views.Home.as_view()),
	2、url(r'^detail-(\d+).html', views.detail),  
	3、url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail) #动态路由
	   
	   PS:
			def detail(request, *args,**kwargs):
				pass
	
	   实战：
			a. 
				url(r'^detail-(\d+)-(\d+).html', views.detail),
				
				def func(request, nid, uid):
					
					pass
			
				def func(request, *args):
					args = (2,9)
					
					
				def func(request, *args, **kwargs):
					args = (2,9)
	   
			b. 
				url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail)
				
				def func(request, nid, uid):
					pass
					
				def funct(request, **kwargs):
					kwargs = {'nid': 1, 'uid': 3}
					
				def func(request, *args, **kwargs):
					args = (2,9)
	4、 name
		
		对URL路由关系进行命名， ***** 以后可以根据此名称生成自己想要的URL *****
		
		url(r'^asdfasdfasdf/', views.index, name='i1'),
		url(r'^yug/(\d+)/(\d+)/', views.index, name='i2'),
		url(r'^buy/(?P<pid>\d+)/(?P<nid>\d+)/', views.index, name='i3'),
		
		
		
		def func(request, *args, **kwargs):
			from django.urls import reverse
			
			url1 = reverse('i1')                              # asdfasdfasdf/
			url2 = reverse('i2', args=(1,2,))                 # yug/1/2/
			url3 = reverse('i3', kwargs={'pid': 1, "nid": 9}) # buy/1/9/
		
		
		xxx.html
			
			{% url "i1" %}               # asdfasdfasdf/
			{% url "i2" 1 2 %}           # yug/1/2/
			{% url "i3" pid=1 nid=9 %}   # buy/1/9/
		
		注：
			# 当前的URL
			request.path_info 
	5、多级路由
		
		project/urls.py
			from django.conf.urls import url,include
			from django.contrib import admin

			urlpatterns = [
				url(r'^cmdb/', include("app01.urls")),
				url(r'^monitor/', include("app02.urls")),
			]
			
		app01/urls.py
			from django.conf.urls import url,include
			from django.contrib import admin
			from app01 import views

			urlpatterns = [
				url(r'^login/', views.login),
			]
			
		app02/urls.py
			from django.conf.urls import url,include
			from django.contrib import admin
			from app02 import views

			urlpatterns = [
				url(r'^login/', views.login),
			]
	
	6、默认值（欠）
	
	7、命名空间（欠）
	
	
二、视图
	1、获取用户请求数据
		request.GET
		request.POST
		request.FILES
			获取上传文件
			obj=request.FILES.get(bbb)
			import os
			file_path=os.path.join('upload',obj.name)
			f=open(file_path,mode='wb')
			for i in chunks();
				f.write(i)
			f.close()
		PS:
			GET:获取数据				
			POST:提交数据
			
	2、checkbox等多选的内容
		request.POST.getlist()
	3、上传文件
		# 上传文件,form标签做特殊设置
		obj = request.FILES.get('fafafa')
		obj.name
		f = open(obj.name, mode='wb')
		for item in obj.chunks():
			f.write(item)
		f.close()
	
	4、FBV & CBV
	   function base view
	   
		url.py
			index -> 函数名
			
		view.py
			def 函数(request):
				...
		====》
		/index/ -> 函数名
			
		/index/ -> 类
		
		====》
		
		建议：两者都用
		
	5、装饰器
		欠

	
三、模板
	
	

四、ORM操作
	select * from tb where id > 1
	# 对应关系
	models.tb.objects.filter(id__gt=1)
	models.tb.objects.filter(id=1)
	models.tb.objects.filter(id__lt=1)
	
	创建类
	
	a. 先写类
		from django.db import models

		# app01_userinfo
		class UserInfo(models.Model):
			# id列，自增，主键
			# 用户名列，字符串类型，指定长度
			username = models.CharField(max_length=32)
			password = models.CharField(max_length=64)
		
	b. 注册APP

		INSTALLED_APPS = [
			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'app01',
		]
	c. 执行命令
		python manage.py  makemigrations
		python manage.py  migrate
		
	d. ********** 注意 ***********
		Django默认使用MySQLdb模块链接MySQL
		主动修改为pymysql，在project同名文件夹下的__init__文件中添加如下代码即可：
			import pymysql
			pymysql.install_as_MySQLdb()
	
	1. 根据类自动创建数据库表
		# app下的models.py
	
		python manage.py  makemigrations
		python manage.py  migrate
		
		
		字段：
			字符串类型
			
			
			数字
			
			
			时间
			
			
			二进制
			
			自增（primary_key=True）
			
		字段的参数：
			null               -> db是否可以为空
			default            -> 默认值
			primary_key        -> 主键
			db_column          -> 列名
			db_index           -> 索引
			unique			   -> 唯一索引
			unique_for_date    -> 
			unique_for_month
			unique_for_year
			auto_now           -> 创建时，自动生成时间
			auto_now_add       -> 更新时，自动更新为当前时间
			
				# obj = UserGroup.objects.filter(id=1).update(caption='CEO')
				# obj = UserGroup.objects.filter(id=1).first()
				# obj.caption = "CEO"
				# obj.save()
				
			choices			  -> django admin中显示下拉框，避免连表查询
			blank             -> django admin是否可以为空
			verbose_name      -> django admin显示字段中文
			editable          -> django admin是否可以被编辑
			error_messages    -> 错误信息欠
			help_text         -> django admin提示
			validators		  -> django form ,自定义错误信息（欠）
			
			
			创建 Django 用户：python manage.py createsuperuser
			
			
			
			
	2. 根据类对数据库表中的数据进行各种操作
	
		一对多：
		
			a. 外检
			b. 
				外键字段_id
			c.
				models.tb.object.create(name='root', user_group_id=1)
				
			d. 
				
				userlist = models.tb.object.all()
				for row in userlist:
					row.id
					row.user_group_id
					row.user_group.caption
					
					
	=================== 作业：用户管理 ====================
	1、用户组的增删改查
	2、用户增删该查
		- 添加必须是对话框
		- 删除必须是对话框
		- 修改，必须显示默认值
		
	3、比较好看的页面
	
	4、预习：
		http://www.cnblogs.com/wupeiqi/articles/5246483.html
