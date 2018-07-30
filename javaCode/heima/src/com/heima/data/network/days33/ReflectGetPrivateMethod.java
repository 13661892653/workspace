package com.heima.data.network.days33;

import java.lang.reflect.Constructor;

/*
 * 	反射获取私有构造方法运行
 * 	不推荐，破坏了程序的封装性，安全性
 * 	
 */
public class ReflectGetPrivateMethod {

	public static void main(String[] args) throws Exception {
		Class c = Class.forName("com.heima.data.jdbc.days29.Sort");
		//Constructor cons=c.getDeclaredConstructors()获取所有权限的构造方法
		//包括private权限的构造方法
		Constructor[] cons = c.getDeclaredConstructors();
		for (Constructor con : cons) {
			System.out.println(con);
		}
		/*
		 * 	获取私有构造方法，指定参数即可
		 */
		Constructor c2 = c.getDeclaredConstructor(int.class, String.class);
		System.out.println(c2);
		//私有方法默认访问报错，c2.setAccessible(true);
		//setAccessible(true)true，则指示反射的对象在 访问的时候应该取消Java语言访问检查
		c2.setAccessible(true);
		Object object = c2.newInstance(20, "戴维");
		System.out.println(object);
	}
}
