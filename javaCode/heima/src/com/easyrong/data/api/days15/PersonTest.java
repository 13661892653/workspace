package com.easyrong.data.api.days15;

public class PersonTest {
	public static void main(String[] args) {
		Person p1=new Person("colby", 20);
		Person p2 =new Person("cl", 30);
		
		boolean b=p1.equals(p2);
		System.out.println("比对结果："+b);
	}
}
