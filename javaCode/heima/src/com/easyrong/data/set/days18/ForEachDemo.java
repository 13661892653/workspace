package com.easyrong.data.set.days18;

import java.util.ArrayList;

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
		function02();
	}
	
	public static void function01() {
		int[] arr= {1,2,3,4,55,66,77};
		for(int i :arr) {
			System.out.println(i);
		}
	}
		
	public static void function02() {
		ArrayList<Person> arr=new ArrayList<Person>();
		arr.add(new Person("colby",20));
		arr.add(new Person("www",25));
		arr.add(new Person("data",30));
		arr.add(new Person("yy",40));
//		for(Person a:arr) {
//			arr.add(new Person("yy",40));
//		}
		for(int i=0;i<arr.size();i++) {
			if(arr.get(i).getName()=="colby") {
				arr.add(new Person("yy",40));
			}
		}
		for(Person a:arr) {
			System.out.println(a);
		}
	}
}
