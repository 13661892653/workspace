package com.easyrong.data.base.days14;

public class PersonTest {
	public static void main(String[] args) {
		operaterPerson(new Person("colby"));
		
		operaterPerson(new Person("cl"));
	}
	
	public static void operaterPerson(Person p) {
		p.eat();
		p.run();
	}
}
