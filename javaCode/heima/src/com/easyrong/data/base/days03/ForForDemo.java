package com.easyrong.data.base.days03;

public class ForForDemo {
    public static void main(String args[]) {
        //局部变量
        //类变量（静态变量）
        //成员变量（非静态变量）

        for (int i = 0; i < 20; i++) {
            for (int j = 1; j < i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
