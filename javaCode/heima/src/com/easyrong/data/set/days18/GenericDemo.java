package com.easyrong.data.set.days18;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;

public class GenericDemo {

	public static void main(String[] args) {
		function01();
	}

	public static void function01() {
		ArrayList<String> arr = new ArrayList<String>();
		HashSet<Integer> set = new HashSet<Integer>();
		arr.add("colby");
		arr.add("cl");
		arr.add("data");

		set.add(1);
		set.add(2);
		set.add(3);

		iterator(arr);
		iterator(set);
	}

	public static void iterator(Collection<?> coll) {// 通配符，String与Integer都可以接收
		Iterator<?> it = coll.iterator();
		while (it.hasNext()) {
			// 不要做强转，强转类型之间会报错
			System.out.println(it.next());
		}
	}

}
