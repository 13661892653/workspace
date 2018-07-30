package com.heima.data.set.days19;

public class Person extends Object {
	private String name;
	private int age;

	public int hashCode() {
		return this.name.hashCode() + age;
	}

	public boolean equals(Object obj) {
		// return (this == obj);
		if (this == obj) {
			return true;
		} else if (obj == null) {
			return false;
		} else if (obj instanceof Person) {
			Person p = (Person) obj;
			boolean b = (this.name.equals(p.name)) && (this.age == p.age);
			return b;
		}
		return false;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public String toString() {
		return "Person [name=" + name + ", age=" + age + "]";
	}

	public Person(String name, int age) {
		super();
		this.name = name;
		this.age = age;
	}

}
