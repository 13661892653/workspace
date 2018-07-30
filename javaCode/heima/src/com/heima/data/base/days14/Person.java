package com.heima.data.base.days14;

public class Person {
	private String name;
	
	public Person(String name) {
		this.name=name;
	}
	
	public void eat() {
		System.out.println(this.name+"正在吃饭！");
	}
	
	public void run() {
		System.out.println(this.name+"正在跑步");
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
}
