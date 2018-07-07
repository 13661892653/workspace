package com.easyrong.data.days10;

public class DevelopTest {
    /*
     *类的继承测试
     *
     *
     */
    public static void main(String args[]){
        Develop d=new Develop();
        d.name="colby";
        d.work();
        d.printName();

        Operation oper=new Operation();
        oper.name="colby";
        oper.work();
        oper.operation();
    }
}
