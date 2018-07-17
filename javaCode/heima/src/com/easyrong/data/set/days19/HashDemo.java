package com.easyrong.data.set.days19;

import java.util.HashSet;

public class HashDemo {
	public static void main(String[] args) {
		function1();
	}

	public static void function1() {
		HashSet<Person> hs = new HashSet<Person>();
		hs.add(new Person("colby", 3000));
		hs.add(new Person("colby", 3000));
		hs.add(new Person("colby", 3000));
		System.out.println(hs);
	}
}
