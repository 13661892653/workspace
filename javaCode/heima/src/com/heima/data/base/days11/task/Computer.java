package com.heima.data.base.days11.task;

public class Computer {
    /*
     *
     */
    public void startComputer(){
        System.out.println("电脑开机！");
    }

    public void closeComputer(){
        System.out.println("电脑关机！");
    }

    public void useUSB(USB usb){
        usb.startUSB();
        usb.closeUSB();
    }
}
