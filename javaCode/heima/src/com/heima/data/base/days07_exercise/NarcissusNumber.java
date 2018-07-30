package com.heima.data.base.days07_exercise;

public class NarcissusNumber {
    public static void main(String args[]) {
        /*
            水仙花数定义：
            3位数本身 = 百位数立方 + 十位数立方 + 个位数立方
        */
        int ge;
        int shi;
        int bai;

        for (int i = 100; i < 1000; i++) {
            ge = i / 100 % 10;
            shi = i / 10 % 10;
            bai = i % 10;
            if (i == ge * ge * ge + shi * shi * shi + bai * bai * bai) {
                System.out.println("满足条件：" + i);
            }
        }
    }
}
