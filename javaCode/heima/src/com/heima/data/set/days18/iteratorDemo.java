package com.heima.data.set.days18;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class iteratorDemo {
	public static void main(String[] args) {
		Collection<String> coll=new ArrayList<String>();//ArrayList集合，可以替换成其他集合
		coll.add("a");
		coll.add("b");
		coll.add("c");
		coll.add("e");
		Iterator<String> it=coll.iterator();//集合中迭代器的使用
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
	}
	
}
