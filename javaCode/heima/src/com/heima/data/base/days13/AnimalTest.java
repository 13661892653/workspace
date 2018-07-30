package com.heima.data.base.days13;


import java.util.concurrent.locks.Lock;

/**
 *
 */
public class AnimalTest {
    public static void main(String args[]) {
        /*
         *com.easyrong.data.days13.AnimalTest
         * */
        Lock l=null;

        Animal a=new Animal(){
            /**
             *
             */
            @Override
            public void eat() {
                System.out.println("动物吃饭");
            }

            @Override
            public void sleep() {
                System.out.println("动物睡觉");
            }
        };
        a.eat();
        a.sleep();
    }
}
