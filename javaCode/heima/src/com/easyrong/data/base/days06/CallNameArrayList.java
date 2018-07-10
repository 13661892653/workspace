package com.easyrong.data.base.days06;

import java.util.ArrayList;
import java.util.Random;

public class CallNameArrayList {
    public static void main(String args[]) {
        ArrayList<Student> array = new ArrayList<Student>();
        add(array);
        printList(array);
        randomCallName(array);
    }

    public static void printList(ArrayList<Student> array) {
        for (int i = 0; i < array.size(); i++) {
            System.out.println(array.get(i).age + " " + array.get(i).name);
        }
    }

    public static void add(ArrayList<Student> array) {
        Student st1 = new Student();
        Student st2 = new Student();
        Student st3 = new Student();
        Student st4 = new Student();
        Student st5 = new Student();

        st1.age = 1001;
        st1.name = "colby1";

        st2.age = 1002;
        st2.name = "colby2";

        st3.age = 1003;
        st3.name = "colby3";

        st4.age = 1004;
        st4.name = "colby4";

        st5.age = 1005;
        st5.name = "colby5";

        array.add(st1);
        array.add(st2);
        array.add(st3);
        array.add(st4);
        array.add(st5);
    }

    public static void randomCallName(ArrayList<Student> array) {
        Random ran = new Random();
        int index = ran.nextInt(array.size());
        int age = array.get(index).age;
        String name = array.get(index).name;
        System.out.println("随机点名：" + name + " " + age);
    }
}
