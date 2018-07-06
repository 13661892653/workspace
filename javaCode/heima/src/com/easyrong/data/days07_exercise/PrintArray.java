package com.easyrong.data.days07_exercise;

public class PrintArray {
    public static void main(String args[]) {
        /*
            打印数组：输出格式如下
            [10,2,30,4,5]
        */
        int[] arr1 = {10, 2, 30, 4, 5};
        printArray(arr1);
    }

    public static void printArray(int[] s) {
        for (int i = 0; i < s.length; i++) {
            if (i == 0) {
                System.out.print("[" + s[i] + ",");
            } else if (i == s.length - 1) {
                System.out.print(s[i] + "]");
            } else {
                System.out.print(s[i] + ",");
            }
        }
    }
}
