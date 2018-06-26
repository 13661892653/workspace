package com.runoob.base;

public class ArrayDemo {
    public static void main(String args[]){
        // dataType[] arrayRefVar;首选方法
        // dataType arrayRefVar[];效果相同，但不是首选方法
        //double[] myList1;         // 首选的方法
        //double myList2[];         // 效果相同，但不是首选方法
        // dataType[] arrayRefVar = new dataType[arraySize];
        // dataType[] arrayRefVar = {value0, value1, ..., valuek};
        // 数组的元素是通过索引访问的。数组索引从 0 开始，
        // 所以索引值从 0 到 arrayRefVar.length-1。
        /**
         * for (double element: myList) {
         *          System.out.println(element);
         *       }
         */
        double[] myList = {1.9, 2.9, 3.4, 3.5};
        // 打印所有数组元素
        for (int i=0;i<myList.length;i++){
            System.out.println("myList["+i+"]:"+myList[i]);
        }

        // 计算所有元素的总和
        double sum=0;
        for (int i=0;i<myList.length;i++){
            sum+=myList[i];
        }
        System.out.println("myList总和："+sum);

        // 查找最大元素
        double max=myList[0];
        for (int i=1;i<myList.length;i++){
            if (max<myList[i]) max=myList[i];
        }
        System.out.println("myList最大自："+max);

        for (Double i: myList) {
            System.out.println(i);
        }

        int[] reverse=reverse(new int[]{3, 1, 2, 6, 4, 2});
        for (int i: reverse) {
            System.out.println(i);
        }
    }

    //通过函数调用数组返回值
    public static int[] reverse(int[] list) {
        int[] result = new int[list.length];

        for (int i = 0, j = result.length - 1; i < list.length; i++, j--) {
            result[j] = list[i];
        }
        return result;
    }
}
