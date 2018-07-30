package com.heima.data.network.days33;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class ReflectGetPublicMethod {

	public static void main(String[] args) throws Exception {
		Class c = Class.forName("com.heima.data.jdbc.days29.Sort");
		getConstructor(c);
		getConstructor2(c);

	}

	public static void getConstructor(Class c) throws NoSuchMethodException, SecurityException, InstantiationException,
			IllegalAccessException, IllegalArgumentException, InvocationTargetException {
		// 获取构造方法，public权限的
		Constructor[] constructors = c.getConstructors();
		for (int i = 0; i < constructors.length; i++) {
			System.out.println(constructors[i]);
		}

		// 获取指定的构造方法
		Constructor constructor = c.getConstructor();
		System.out.println(constructor);

		// 运行空参构造方法
		Object obj = constructor.newInstance();
		System.out.println(obj);
		
		
	}
	public static void getConstructor2(Class<?> c) throws Exception{
		//getConstructor(Class<?>... parameterTypes)
		System.out.println("=========================getConstructor2======================");
		Constructor<?> c2=c.getConstructor(int.class , String.class , String.class , double.class);
		System.out.println(c2.newInstance(20,"蔬菜","水果",500));
		
		//class类中定义方法，T newInstance()直接创建被反射类的对象的实例
		Object obj=c.newInstance();
		System.out.println(obj);
	}

}
