package com.easyrong.data.days07_exercise;

public class ReverseArray {
    public static void main(String args[]) {
        /*
         *
         *
         * */
        int[] arr1 = {101, 200, 90, 1, 7980, 55, 0, 1000};
        reverseArray(arr1);
    }

    public static void reverseArray(int[] arr1) {
        for (int i = 0; i < arr1.length / 2; i++) {

            int temp = arr1[i];
            arr1[i] = arr1[arr1.length - i - 1];
            arr1[arr1.length - i - 1] = temp;

        }
        //数组打印，调用PrintArray类的方法
        PrintArray pa = new PrintArray();
        pa.printArray(arr1);
    }
}
