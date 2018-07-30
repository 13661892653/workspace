package com.heima.data.base.days12;

public class Person {
    private String name;
    private int age;

    public Person(String sex) {
        System.out.println("空的构造方法。"+sex);
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}
