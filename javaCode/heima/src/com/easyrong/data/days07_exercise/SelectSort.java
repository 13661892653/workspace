package com.easyrong.data.days07_exercise;

public class SelectSort {
    public static void main(String args[]) {
        /*
         * 【选择排序】实现逻辑
         * 两两比较
         * */
        int[] initArray = {200, 100, 66, 999, 10};
        selectSort(initArray);
    }

    public static void selectSort(int[] initArray) {
        int temp;
        PrintArray pt = new PrintArray();
        pt.printArray(initArray);
        for (int i = 0; i < initArray.length - 1; i++) {
            for (int j = i + 1; j < initArray.length; j++) {
                if (initArray[i] > initArray[j]) {
                    temp = initArray[i];
                    initArray[i] = initArray[j];
                    initArray[j] = temp;
                }
            }
        }
        System.out.println();
        pt.printArray(initArray);
    }

}
