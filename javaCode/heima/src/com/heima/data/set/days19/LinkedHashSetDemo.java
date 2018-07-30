package com.heima.data.set.days19;

import java.util.LinkedHashSet;
public class LinkedHashSetDemo {
	public static void main(String[] args) {
		function01();
	}
	
	public static void function01() {
		//LinkedHashSet有序不重复
		LinkedHashSet<String> linkedHashSet=new LinkedHashSet<String>();
		linkedHashSet.add("aaa");
		linkedHashSet.add("bbb");
		linkedHashSet.add("ccc");
		linkedHashSet.add("ccc");
		System.out.println(linkedHashSet);
	}
}
