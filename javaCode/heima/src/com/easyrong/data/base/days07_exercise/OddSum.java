package com.easyrong.data.base.days07_exercise;

public class OddSum {

    public static void main(String args[]) {
        /*
            100以内奇数求和
        */
        int sum = 0;
        for (int i = 1; i < 100; i++) {
            if (i % 2 == 1) {
                sum += i;
            }
        }
        System.out.println("100以内的奇数和为：" + sum);
    }
}
