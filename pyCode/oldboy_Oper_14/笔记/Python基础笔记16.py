 switch (){
    case:ddddd:
        console.log(ddd);
        break;
    case:ddddd:
        console.log(ddd);
        break;
    default:
        语句;
 }
 
 JavaScript
        函数
        普通函数
                function func(arg){
                
                }
        
        匿名函数
                没有名字的函数叫匿名函数
                setIntervar(function(){
                        函数体;
                })
       自执行函数:args形参，1为实参
                (function(args){
                        console.log(args);
                )(1)
                
        序列化：
                JSON.stringify(li) 将对象转化成为字符床
                
                JSON.parse(s) 将字符串转成对象类型
        转义
        Python     
        eval(表达式)
        exec(执行代码) 没有返回值
        javaScript:
                eval 是Python的集合，即：支持表达式和执行代码两块
        
        时间模块
                var d = new Date()
                d.setMinutes()+4 /* 设置时间*/
                d.getetMinutes() /* 获取时间*/
        作用域
                1、其他语言以{代码块}作为作用域
                2、Python里边的作用域以{函数}为单位        
                3、JavaScript的作用域跟Python一样，以函数为单位
           
	变量向上查找
	xo=1;/*标记1*/
	function func(){
		var xo=2;/*标记2*/
		function inner(){
			var xo = 3;/*标记3*/
			console.log(xo)
		}
	}
	如果标记3的xo有定义，则输出3，如果标记3没定义，标记2有定义，则输出2，同理，如果都没有定义则报错。
                
	JavaScript面向对象
	function foo(name){
		this.name = name	
	}
	var obj=new foo('Guo');
	a、this关键字代指对象
	b、new创建一个对象
	
DOM学习：
	innerText：
	document.getElementById('i1).innerText 获取文本
	innerHTML：
	document.getElementById('i1).innerHTML 获取全部内容
	
	value
		input 	获取input的值
		select	获取select选中的值
		textarea
              搜索框的示例：
	function Focus(){
		var tag=document.getElementById('id1');
		var val=tag.value;
		if(val == "请输入关键字"){
			tag.value="";
		}
	}
	function Blur(){
		var tag=document.getElementById('id1');
		var val=tag.value;
		if(val==""){
			tag.value="请输入关键字";
		}
	}
               函数方法命名都是驼峰命名，如className,第一个单词首字母小写，之后其他单词首字母大写
	var obj=document.getElementById('id1').classList
	CSS样式操作
	var obj_style=obj.style.      
                
	属性操作：
		getAttribute 获取属性值
		setAttribute 设置属性值
		obj.setAttribute('属性名','属性值')
		obj.setAttribute('属性名','属性值')
	创建标签
		tag.createElement('标签名称')
		a.字符串形式
		b.对象的方式
		tag.createElement('dvi') #创建div标签
		
	提交表单：
	<script>
		function submitForm(){
			document.getElementById('form1').submit()
		}
	</script>
	
	其他操作
		confirm:确认框，返回True或者False
		location.href获取当前页面的url
		location.href=""#设置当前url
		location.href=reload #刷新页面
		si=setInterval(function(){},5000)
		clearInterval(si)
		
		si=setTimeout(function(){},5000)
		clearTimeout(si)
	
	事件
		onclick 点击
		onblur 光标移开
		onfocus 光标插进去
		绑定事件两种方式
			a.直接标签绑定
			b.先获取Dom对象，然后进行绑定
			document.getElementById('xx').onclick
			document.getElementById('xx').onfocus
		this 当前触发事件的标签
			a.事件的第一种绑定方式
			<input type="button" onclick="clickOn(this)">
			function clickOn(self){
				//self 当前点击的标签
			}
			b.事件的第二种绑定方式
			<input id="i1" type=button>
			document.getElementById('i1').onclick=function(){
				//this代指当前点击的标签
			}
			c.事件的第三种绑定方式
			var mydiv=document.getElementById('form1')
				mydiv.addEventListener('click',function(){
				console.log('aa')
				},false)
			#false:冒泡模型
			#true:捕捉模型，默认不写就是冒泡模型
			
		//作用域的示例
		var myTrs =document.getElementByTagName('tr');
		var len=myTrs.length;
		for(var i=0;i<len;i++){
			myTrs[i].onmouseover=function(){
				#错误写法 myTrs[i].style.backgoundColor='red'
				this.style.backgoundColor='red'
			}
		}
		
		作用域-词法分析
			分析完之后，再赋值。
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	