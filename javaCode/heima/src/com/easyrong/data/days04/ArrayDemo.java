package com.easyrong.data.days04;

public class ArrayDemo {
    public static void main(String args[]) {
        //数组类型[] 数组名=new 数据类型[元素个数或者数组长度]
        // int[] a=new int[10];
        int[] a=new int[10];
        for (int i=0;i<a.length;i++){
            a[i]=i;
        }

        for (int j=0;j<a.length;j++){
            if (a[j]%2==1){
                System.out.println("奇数，a["+j+"]="+a[j]);
            }else{
                System.out.println("偶数隐藏，不打印！");
            }

        }

    }
}
