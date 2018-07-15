package com.easyrong.data.set.days18;

import java.util.ArrayList;
import java.util.Collection;

public class CollectionDermo {
	public static void main(String[] args) {
		
		function01();
	}
	
	public static void function01() {
		Collection<String> coll=new ArrayList<String>();//多态调用
		coll.add("www");
		coll.add("data");
		coll.add("colby");
		boolean b=coll.contains("colby");//判断元素是否包含在集合中
		System.out.println(b);
	}
}
