package com.easyrong.data.set.days19;

import java.util.HashSet;

public class HashSetDemo01 extends Object {
	public static void main(String[] args) {
		HashSet<Person> setPerson=new HashSet<Person>();
		setPerson.add(new Person("colby", 30));
		setPerson.add(new Person("abc", 20));
		setPerson.add(new Person("def", 10));
		setPerson.add(new Person("hjk", 40));
		setPerson.add(new Person("hjk", 40));
		System.out.println(setPerson);
	}
}
