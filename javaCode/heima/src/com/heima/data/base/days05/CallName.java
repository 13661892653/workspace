package com.heima.data.base.days05;

import java.util.Random;

public class CallName {
    public static void main(String args[]) {
        String[] names = new String[8];
        addStudent(names);
        printStudentName(names);
        randomCallName(names);
    }

    public static void randomCallName(String names[]) {
        Random ran = new Random();
        int index = ran.nextInt(names.length);
        System.out.println("随机点名：" + names[index]);
    }

    public static void addStudent(String[] names) {
        names[0] = "A";
        names[1] = "B";
        names[2] = "C";
        names[3] = "D";
        names[4] = "E";
        names[5] = "F";
        names[6] = "G";
        names[7] = "H";
        System.out.println("names数组增加值成功！");
    }

    public static void printStudentName(String[] names) {
        System.out.println("打印数组names...");
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }
    }


}
