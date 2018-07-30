package com.heima.data.set.days20;

import java.util.HashMap;
import java.util.Set;

public class MapMapDemo {
	public static void main(String[] args) {
		function01();
	}
	
	public static void function01() {
		HashMap<String, HashMap<String,String>> czbk=new HashMap<String,HashMap<String,String>>();
		HashMap<String,String> javase=new HashMap<String,String>();
		HashMap<String,String> javaee=new HashMap<String,String>();
		javase.put("001", "张三");
		javase.put("002", "李四");
		javaee.put("003", "王五");
		javaee.put("004", "赵六");
		czbk.put("基础班", javase);
		czbk.put("就业班", javaee);
		Set<String> classSet=czbk.keySet();
		for(String className:classSet) {
			HashMap<String,String> StudentMap=czbk.get(className);
			Set<String> studentSet=StudentMap.keySet();
			for(String StudentNum:studentSet) {
				System.out.println(className+"->"+StudentNum+"="+StudentMap.get(StudentNum));
			}
		}		
	}
}
