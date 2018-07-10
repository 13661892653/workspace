package com.easyrong.data.base.days11.task;

public class Mouse implements USB{
    /*
     *
     */

    @Override
    public void startUSB() {
        System.out.println("鼠标打开USB！");
    }

    @Override
    public void closeUSB() {
        System.out.println("鼠标关闭USB！");
    }
}
