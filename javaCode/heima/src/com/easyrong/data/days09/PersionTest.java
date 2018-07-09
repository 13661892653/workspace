package com.easyrong.data.days09;

public class PersionTest {
    public static void main(String[] args){
        Person p=new Person();
        p.setAge(30);
        p.setName("colby");
        p.speak();

        Person p1=new Person();
        Person p2=new Person();
        p1.setAge(30);
        p2.setAge(30);
        boolean b=p1.compare(p2);
        System.out.println("年龄比较结果："+b);
    }
}
