 jQuery
	模块<->类库
	DOM/BOM/JavaScript的类库

在线帮助文档：http://jquery.cuishifeng.cn/
	一、查找元素
	选择器
		1.id
			$('#id')
		2.class
			$('.class')
		3.标签
			$('a')
		4.多个标签用逗号隔开
			$('a,.class,#id')
		5.层级，a标签下所有div标签-子子孙孙
			$('#id div')#空格子子孙孙，
			$('#id>div')#>只查找儿子
		6.基本筛选器
			：first
			：last
			：not(selector)
			：eq()
			...
			$(this).next()      #下一个
			$(this).prev()      #上一个
			$(this).parent()    #父
			$(this).children()  #孩子
			$('#i1').siblings() #兄弟
			$('#i1').find('#i1') #子子孙孙中查找
			// . . .
			//
			$('#i1').addClass(..) #添加样式
			$('#i1').removeClass(..) #移除样式
			
			// 链式编程
			// $(...).click(function(){
			//     this..
			// })


			//            $(this).next().removeClass('hide');
			//            $(this).parent().siblings().find('.content').addClass('hide')

			样例，一行就实现：$(this).next().removeClass('hide').parent().siblings().find('.content').addClass('hide')
		7.属性
			$('[active]') 具有active属性的标签
			$('[active]="colby"')具有active属性等于colby的标签
		案例：
			jQuery实现全选反选
			function checkAll(){
				$('#tb :checkbox').prop('checked',true);
			}

			function cancelAll(){
				$('#tb :checkbox').prop('checked',false);
			}
			function reverse(){
				$('#tb :checkbox').each(function(k){
					if(this.checked){
						this.checked=false
					}else{
						this.checked=true
					}
				})
			}
		筛选器
			$('#i1').next()      #下一个
				$('#i1').nextAll()      #当前后面的所有
				$('#i1').nextUntil()      #下一个直到谁
			$('#i1').prev()      #上一个
				$('#i1').prevAll()      #当前前面所有
				$('#i1').prevUntil()      #上一个直到谁
			$('#i1').parent()    #父
				$('#i1').parents()    #找到其所有父辈，直到顶级节点
			$('#i1').children()  #孩子
			$('#i1').siblings() #兄弟
			$('#i1').find('#i1') #子子孙孙中查找
			$('#i1').find('#i1') #子子孙孙中查找
			$('#i1').find('#i1') #子子孙孙中查找
		样式操作
			addClass('hide') #增加
			removeClass('hide') #移除
			toggleClass('hide')#存在移除，不存在增加
		属性操作:
			
	
	
	
	
	
	
	二、操作元素
	
