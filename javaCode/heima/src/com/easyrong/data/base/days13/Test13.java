package com.easyrong.data.base.days13;

import com.easyrong.data.days09.Person;

public class Test13 {
    public static void main(String args[]) {
        /*
         *
         *
         */
        PersonStaticDemo p1 =new PersonStaticDemo();
        PersonStaticDemo p2 =new PersonStaticDemo();
        p1.name="colby";
        p2.name="bobby";
        p1.classname="测试数据";
        System.out.println(p1.name+" "+p2.name+" "+p2.classname);
    }
}
