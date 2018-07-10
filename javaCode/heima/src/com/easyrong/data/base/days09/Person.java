package com.easyrong.data.base.days09;

public class Person {

    private String name;
    private int age;

    public void setName(String name){
        this.name=name;
    }

    public void setAge(int age){
        this.age=age;
    }

    public String getName(){
        return this.name;
    }

    public int getAge(){
        return this.age;
    }

    public void speak(){
        String name="demo";
        int age=20;
        System.out.println(name+age);
        System.out.println("姓名："+this.name+" 年龄："+this.age);
    }

    public boolean compare(Person p){
        return this.age==p.age;
    }
}
