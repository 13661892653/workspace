package com.easyrong.data.set.days18;
/*
 * 
 *	@author Administrator
 *	JDK1.5新增特性
 * 	实现Iterable这个接口，可以调用for增强循环
 * 	格式：for(数据类型 变量名：数组或者集合){
 * 	语句;
 * }
 */
public class ForEachDemo {
	public static void main(String[] args) {
		function01();
	}
	
	public static void function01() {
		int[] arr= {1,2,3,4,55,66,77};
		for(int i :arr) {
			System.out.println(i);
		}
	}
}
