package com.easyrong.data.days06;

import java.util.ArrayList;

public class ArrayListDemo {
    public static void main(String args[]) {
        //创建引用类型的变量
        //数据类型<集合存储的数据类型> 变量名=new 数据类型<>();
        //变量名.方法
        //集合不存储基本类型，只存储引用类型，8个基本类型对应8个引用类型
        ArrayList<String> array1 = new ArrayList<String>();
        ArrayList<Integer> array2 = new ArrayList<Integer>();
        ArrayList<Character> array3 = new ArrayList<Character>();

        array1.add("www");
        array1.add("easyrong");
        array1.add("com");
        //指定位置新增元素
        array1.add(2, "colby");

        //修改指定位置的元素
        array1.set(2, "colby2");

        array1.remove(3);

        String j;
        for (int i = 0; i < array1.size(); i++) {
            j = array1.get(i);
            System.out.println(j);
        }
        array1.clear();

        for (int i = 0; i < array1.size(); i++) {
            System.out.println("array1:" + array1.get(i));
        }
    }
}
