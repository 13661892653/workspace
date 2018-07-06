package com.easyrong.data.days07_exercise;

public class BubbleSort {
    public static void main(String args[]) {
        /*
         * 【冒泡排序】实现逻辑
         * 相邻两个元素比较
         * */
        int[] initArray = {200, 100, 66, 999, 10, 1, 10000};
        ubbleSort(initArray);
    }

    public static void ubbleSort(int[] initArray) {
        int temp;
        PrintArray pt = new PrintArray();
        pt.printArray(initArray);
        for (int i = 0; i < initArray.length - 1; i++) {
            for (int j = 0; j < initArray.length - i - 1; j++) {
                if (initArray[j] > initArray[j + 1]) {
                    temp = initArray[j];
                    initArray[j] = initArray[j + 1];
                    initArray[j + 1] = temp;
                }
            }
        }
        System.out.println();
        pt.printArray(initArray);
    }
}
