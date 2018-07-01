package com.runoob.extend;

public class Animals {
    public static void main(String[] args) {
        show(new Cats());  // 以 Cat 对象调用 show 方法
        show(new Dogs());  // 以 Dog 对象调用 show 方法

        AnimalAbs a = new Cats();  // 向上转型
        a.eat();               // 调用的是 Cat 的 eat
        Cats c = (Cats)a;        // 向下转型
        c.work();        // 调用的是 Cat 的 work
    }

    public static void show(AnimalAbs a)  {
        a.eat();
        // 类型判断
        if (a instanceof Cats)  {  // 猫做的事情
            Cats c = (Cats)a;
            c.work();
        } else if (a instanceof Dogs) { // 狗做的事情
            Dogs c = (Dogs)a;
            c.work();
        }
    }
}

abstract class AnimalAbs {
    abstract void eat();
}

class Cats extends AnimalAbs {
    public void eat() {
        System.out.println("吃鱼");
    }
    public void work() {
        System.out.println("抓老鼠");
    }
}

class Dogs extends AnimalAbs {
    public void eat() {
        System.out.println("吃骨头");
    }
    public void work() {
        System.out.println("看家");
    }
}