package com.heima.data.network.days33;

import com.heima.data.io.days25.Person;

public class ReflectDemo {
	public static void main(String[] args) throws ClassNotFoundException {
		Person person=new Person("colby", 20);
		//对象获取类名第一种方法
		System.out.println(person.getClass());
		
		//类名获取类名第二种方法
		Class<Person> c1=Person.class;
		System.out.println(c1);
		
		//Class类的静态方法获取forName（字符串的类名）
		Class<?> c2=Class.forName("com.heima.data.io.days25.Person");
		System.out.println(c2);
	}
	
}
