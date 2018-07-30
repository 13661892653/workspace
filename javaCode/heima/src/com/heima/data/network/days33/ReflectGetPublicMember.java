package com.heima.data.network.days33;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class ReflectGetPublicMember {
	public static void main(String args[]) throws Exception{
		Class c = Class.forName("com.heima.data.jdbc.days29.Sort");
		
		System.out.println("//获取class文件中的所有公共的成员变量==============================");
		Object obj=c.newInstance();
		Field[] f=c.getFields();
		for(Field field:f){
			System.out.println(field);
		}
		
		System.out.println("//获取指定的成员变量String name===========================");
		//获取指定的成员变量String name
		Field field=c.getField("sname");
		field.set(obj, "colby");
		System.out.println(obj);
		
		System.out.println("//获取指定的成员方法==========================");
		//获取全部的public成员方法
		Method[] ms=c.getMethods();
		for(Method m:ms) {
			System.out.println(m);
		}
		
		System.out.println("//获取指定的成员方法 getSid()==========================");
		//获取指定的成员方法 getSid()
		Method m2=c.getMethod("getSid");
		System.out.println(m2);
		//执行获取到的成员方法
		m2.invoke(obj);
		
		//获取带参数的指定成员方法名称
		Method m3=c.getMethod("setSdesc",String.class);
		System.out.println(m3);
		//执行获取到的成员方法
		m3.invoke(obj,"setSdesc方法，传入的参数");
	}
}
