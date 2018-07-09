package com.easyrong.data.days11.task;

public class USBTest {
    /*
     *
     */

    public static void main(String[] args){
        Computer com=new Computer();

        com.startComputer();
        com.useUSB(new Mouse());
        com.useUSB(new KeyBoard());

        com.closeComputer();
    }
}
