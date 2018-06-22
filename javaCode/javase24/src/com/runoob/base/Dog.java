package com.runoob.base;

public class Dog {
    String breed;
    int age;
    String color;

    public Dog(String name){
        System.out.println(name+",您好！");
    }
    void barking(){

    }
    void hungry(){
        System.out.println(",我好饿！");
    }
    void sleeping(){

    }
    public static void main(String args[]){
        Dog dog=new Dog("colby");
        dog.hungry();
    }
}
