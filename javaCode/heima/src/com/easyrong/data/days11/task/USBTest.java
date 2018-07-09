package com.easyrong.data.days11.task;
import java.sql.Driver;
import java.sql.DriverManager;

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
