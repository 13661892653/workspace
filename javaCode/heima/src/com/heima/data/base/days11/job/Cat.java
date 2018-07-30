package com.heima.data.base.days11.job;

public class Cat extends Animal {
    /*
     *
     */

    @Override
    public void eat() {
        System.out.println("猫吃猫粮，没有鱼吃哈。");
    }

    public void catchMouse() {
        System.out.println("猫抓老鼠。");
    }
}
