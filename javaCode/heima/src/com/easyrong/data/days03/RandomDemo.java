package com.easyrong.data.days03;

import java.util.Random;

public class RandomDemo {
    public static void main(String args[]) {
        // 局部变量
        // 类变量（静态变量）
        // 成员变量（非静态变量）
        Random random = new Random();
        // 生成0到10000的随机数
        System.out.println(random.nextInt(10000));


    }
}
