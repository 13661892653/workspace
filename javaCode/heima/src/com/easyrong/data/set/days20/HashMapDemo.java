package com.easyrong.data.set.days20;

import java.util.HashMap;

public class HashMapDemo {

	public static void main(String[] args) {
		function01();
		function02();
	}

	public static void function01() {
		HashMap<String, Person> hashMap = new HashMap<String, Person>();
		hashMap.put("ID0001", new Person("colby", 30));
		hashMap.put("ID0002", new Person("engs", 120));
		hashMap.put("ID0003", new Person("maks", 120));
		hashMap.put("ID0004", new Person("nina", 31));

		for (String key : hashMap.keySet()) {
			System.out.println(key + ":" + hashMap.get(key).getName() + " " + hashMap.get(key).getAge());
		}
	}

	public static void function02() {
		HashMap<Person, String> hashMap = new HashMap<Person, String>();
		hashMap.put(new Person("colby", 30), "ID0001");
		hashMap.put(new Person("engs", 30), "ID0002");
		hashMap.put(new Person("maks", 30), "ID0003");
		hashMap.put(new Person("Lee", 30), "ID0004");
		System.out.println("====================================");
		for (Person key : hashMap.keySet()) {
			System.out.println(key.getName()
					+" "+key.getAge()
					+" "+hashMap.get(key));
		}
	}
}