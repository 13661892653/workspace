day22

知识点概要
    - Session
    - CSRF
    - Model操作
    - Form验证（ModelForm）
    - 中间件
    - 缓存
    - 信号


内容详细：

1. Session
	基于Cookie做用户验证时：敏感信息不适合放在cookie中
	

    a. Session原理
		Cookie是保存在用户浏览器端的键值对
		Session是保存在服务器端的键值对
	
    b. Cookie和Session对比
    
    c. Session配置(缺少cache)
    
    d. 示例：实现两周自动登陆
            - request.session.set_expiry(60*10)
            - SESSION_SAVE_EVERY_REQUEST = True

    PS: cookie中不设置超时时间，则表示关闭浏览器自动清除
	
	
	- session依赖于cookie
	- 服务器session
		request.session.get()
		request.session[x] = x
		
		request.session.clear()
		
	- 配置文件中设置默认操作（通用配置）：
		SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
		SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
		SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
		SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
		SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
		SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
		SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
		# set_cookie('k',123)
		SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）

	- 引擎的配置
	

2. CSRF
    a. CSRF原理

    b. 无CSRF时存在隐患

    c. Form提交（CSRF）

    d. Ajax提交（CSRF）
       CSRF请求头 X-CSRFToken
	   
	   
6. 中间件
	settings文件中的MIDDLEWARE[]都是中间件
	
7. 缓存
	5种配置
	
	3种应用：
		全局
			
		视图函数
			
		模板
			
8. 信号
    - 内置信号
	- 自定义
		 - 定义信号
		 - 出发信号
		 - 信号中注册函数
	
3. Model操作
    
    a. 字段类型 + 参数

    b. 连表字段 + 参数

    c. Meta

    d. SQL操作：
        - 基本增删改查
        - 进阶操作
        - 正反查询
        - 其他操作

    e. 验证（弱）

4. Form操作
	完成：
		- 验证用户请求
		- 生成HTML
		  （保留上一次提交的数据）
		
	自定义：
		- 类
		- 字段（校验）
		- 插件（生成HTML）
		
	初始化操作：
		
	
	
============= 作业:xxxoo管理 =============
用户验证：session
新URL：Form验证
中间件：IP过滤
信号：记录操作
CSRF：
	
	
	
	
	
	
	
	
	
	
	
    a. Form验证用户请求

    b. Form生成HTML

    c. Form字段详细（自定义字段，Model...） + 插件

    d. 自定义验证(钩子以及__all__)

    e. 注册示例：
         用户名、密码、邮箱、手机号（RegexValidator或RegexField）、性别、爱好、城市
    
    f. 初始化值

5. ModelForm

    a. Model+Form功能集合

    b. save

    c. save + save_m2m
