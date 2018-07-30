package com.heima.data.network.days33;

import java.lang.reflect.Method;
import java.util.ArrayList;

public class ReflectRemoveE {
	public static void main(String[] args) throws Exception {
		ArrayList<String> arr=new ArrayList<String>();
		Class<?> c = Class.forName("java.util.ArrayList");
		Method method=c.getMethod("add", Object.class);
		method.invoke(arr, 2000);
		method.invoke(arr, 3000);
		method.invoke(arr, 5000);
		System.out.println(arr);
	}
}
