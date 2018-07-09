package com.easyrong.data.days12.job;

public class Cat extends Animal {
    String name;
    String color;

    public Cat(String name, String color) {
        super(name, color);
        System.out.println("Cat:" + name + "  " + color);
        this.name = name;
        this.color = color;
        this.active();
    }

    public void active() {
        System.out.println("active:" + this.name + "  " + this.color);
    }
}
