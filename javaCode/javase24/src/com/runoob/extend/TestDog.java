package com.runoob.extend;


public class TestDog{
    public static void main(String args[]){
        AnimalAll a = new AnimalAll(); // Animal 对象
        Tigger t = new Tigger(); // Dog 对象

        a.move();// 执行 AnimalAll 类的方法

        t.move();//执行 Tigger 类的方法

        t.bark();
    }
}

class AnimalAll{
    public void move(){
        System.out.println("动物可以移动");
    }

}

class Tigger extends AnimalAll{
    public void move(){
        super.move();
        System.out.println("老虎可以跑和走");
    }

    public void bark(){
        System.out.println("老虎可以嚎叫");
    }
}