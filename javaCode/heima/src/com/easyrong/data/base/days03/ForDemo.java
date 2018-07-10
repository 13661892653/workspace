package com.easyrong.data.base.days03;

public class ForDemo {
    public static void main(String args[]) {
        //局部变量
        //类变量（静态变量）
        //成员变量（非静态变量）
        int sum = 0;
        for (int i = 0; i < 1000; i++) {
            sum = sum + i;
        }
        System.out.println(sum);
    }
}
