package com.easyrong.data.base.days11.job;

public class AnimalTest {
    /*
     * 1、实现动物和cat、dog多态调用
     * 2、做类型的强制转换，调用子类的特有功能
     */
    public static void main(String args[]) {
        Animal a1 = new Cat();
        Animal a2 = new Dog();

        a1.eat();
        a2.eat();

        //类型向下转换
        ((Cat) a1).catchMouse();
        ((Dog) a2).lookHome();
    }
}
