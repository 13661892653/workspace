package com.easyrong.data.days10.job;

public class EngineerTest {
    /*
     *
     */
    public static void main(String[] args){
        JavaEE ee=new JavaEE();
        ee.setId("10001");
        ee.setName("张三");
        ee.work();

        Android and=new Android();
        and.setId("10002");
        and.setName("李四");
        and.work();

        HardwareEngineer hd=new HardwareEngineer();
        hd.setId("10003");
        hd.setName("王五");
        hd.work();

        NetworkEngineer nw=new NetworkEngineer();
        nw.setId("10004");
        nw.setName("赵六");
        nw.work();
    }
}
