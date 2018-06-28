package com.runoob.extend;

public class ExtendsDemo {
    public static void main(String args[]) {
        // class 父类 {
        //  }
        // class 子类 extends 父类 {
        //  }
        // final 关键字声明类可以把类定义为不能继承的，即最终类；或者用于修饰方法，该方法不能被子类重写：
        // 修饰符(public/private/default/protected) final 返回值类型 方法名(){//方法体}
        Animal a=new Animal();
        a.eat();
        Dog d=new Dog();
        d.eatTest();
    }
}

class Animal {
    void eat() {
        System.out.println("animal : eat");
    }
}

class Dog extends Animal {
    void eat() {
        System.out.println("dog : eat");
    }
    void eatTest() {
        this.eat();   // this 调用自己的方法
        super.eat();  // super 调用父类方法
    }
}
