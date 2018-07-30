package com.heima.data.base.days11.job;

public class Dog extends Animal {
    /*
     *
     */

    @Override
    public void eat() {
        System.out.println("狗吃狗粮，没有粑粑吃哈。");
    }

    public void lookHome() {
        System.out.println("狗看家。");
    }
}
