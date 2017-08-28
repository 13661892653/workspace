上节作业问题：
    1、css重用
        
        <style>
            如果整个页面的宽度 > 900px时：
            {
                .c{
                   共有 
                }
                .c1{
                    独有
                }
            }
            
            .c2{
                独有
            }
        </style>
        
        <div class='c c1'></div>
        <div class='c c2'></div>
    2、自适应 和 改变大小变形
        左右滚动条的出现
        宽度，百分比
        
        页面最外层：像素的宽度 => 最外层设置绝对宽度
        
        
        自适应：media
        
    3、默认img标签，有一个1px的边框
        img{
            border: 0;
        }
    
    4、作业中的数量输入框
    
上节内容回顾
    1、块级和行内
    2、form标签
            <form action='http://sssss' methed='GET' enctype='multi'>
                <div>asdfasdf</div>
                <input type='text' name='q' />
                <input type='text' name='b' />
                # 上传文件
                <input type='file' name='f' />
                <input type='submit' />
            </form>
            GET: http://sssss?q=用户输入的值
                 http://sssss?q=用户输入的值&b=用户输入的内容
                 
            POST：
                请求头
                请求内容
    3、display: block;inline;inline-block
    4、float：
        <div>
            <div style='float:left;'>f</div>
            <div style='clear:both;'></div>
        </div>

    5、margin: 0 auto;
    6、padding, ---> 自身发生变化
    
    
CSS补充
    position:
        a. fiexd => 固定在页面的某个位置left/right/top/bottom
        
        b. relative + absolute
        
            <div style='position:relative;'>
                <div style='position:absolute;top:0;left:0;'></div>
            </div>

    opcity: 0.5 透明度
    z-index: 层级顺序
    overflow: 超过直接滚动条auto,超过直接隐藏hidden
    hover：鼠标移动上去标签颜色变化.pg-header .menu.hover{
        background-color:blue
    }
    
    background-image:url('image/4.gif'); # 默认，div大，图片重复访
    background-repeat: repeat-y 竖着重复;repeat-x横着重复;渐变色小竖条迭代整个屏幕
    background-position-x:扣洞，移动图像，横向移动
    background-position-y:扣洞，移动图像，纵向移动
    
    示例：输入框

JavaScript
    独立的语言，浏览器具有js解释器
    
    JavaScript代码存在形式：
        - Head中
                <script>
                    //javascript代码
                    alert(123);
                </script>
                
                <script type="text/javascript">
                    //javascript代码
                    alert(123);
                </script>
        - 文件
            <script src='js文件路径'> </script>
            
        PS: JS代码需要放置在 <body>标签内部的最下方
        
    注释
        当行注释 //
        多行注释  /*     */
        
    变量：
        
        python：
            name = 'alex'
        JavaScript:
            name = 'alex'     # 全局变量
            var name = 'eric' # 局部变量
        
    写Js代码：
        - html文件中编写
        - 临时，浏览器的终端 console
        
          
    基本数据类型
        数字
            a = 18;
        字符串
            a = "alex"
            a.chartAt(索引位置)
            a.substring(起始位置，结束位置)
            a.lenght    获取当前字符串长度
            ...
        列表(数组)
            a = [11,22,33]
            
        字典
            a = {'k1':'v1','k2':'v2'}
        布尔类型
            小写
      
    for循环
        1. 循环时，循环的元素是索引
        
            a = [11,22,33,44]
            for(var item in a){
                console.log(item);
            }
            
            a = {'k1':'v1','k2':'v2'}
            for(var item in a){
                console.log(item);
            }
            
        2. 
            for(var i=0;i<10;i=i+1){
                
            }
            
            a = [11,22,33,44]
            for(var i=0;i<a.length;i=i+1){
                
            }
            
            不支持字典的循环
    
      
    条件语句
        if(条件){
        
        }else if(条件){
            
        }else if(条件){
            
        }else{
            
        }
        
        ==   值相等
        ===  值和类型都相等
        &&   and
        ||   or
        
    
    函数：
    
        
        function 函数名(a,b,c){
        
        }
        
        函数名(1,2,3)
    
       
    
    

Dom
    1、找到标签
        获取单个元素        document.getElementById('i1')
        获取多个元素（列表）document.getElementsByTagName('div')
        获取多个元素（列表）document.getElementsByClassName('c1')
        a. 直接找
            document.getElementById             根据ID获取一个标签
            document.getElementsByName          根据name属性获取标签集合
            document.getElementsByClassName     根据class属性获取标签集合
            document.getElementsByTagName       根据标签名获取标签集合
        
        b. 间接
            tag = document.getElementById('i1')
            
            parentElement           // 父节点标签元素
            children                // 所有子标签
            firstElementChild       // 第一个子标签元素
            lastElementChild        // 最后一个子标签元素
            nextElementtSibling     // 下一个兄弟标签元素
            previousElementSibling  // 上一个兄弟标签元素
            
    2、操作标签
        
        a. innerText
            
            获取标签中的文本内容
            标签.innerText
            
            对标签内部文本进行重新复制
            
            标签.innerText = ""
            
        b. className
            tag.className =》 直接整体做操作
            tag.classList.add('样式名')   添加指定样式
            tag.classList.remove('样式名')   删除指定样式
    
            PS：
            
                <div onclick='func();'>点我</div>
                <script>
                    function func(){
                    
                    }
                
                </script>
    
        c. checkbox  
                获取值
                checkbox对象.checked
                设置值
                checkbox对象.checked = true
    
    
    
作业：
    1、登录、注册，练习：position
    2、后台管理页面
        - 左侧菜单
        - 右边表格，全选反向，模态框，返回顶部
    3、商城页面
    
 