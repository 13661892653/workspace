package com.runoob.base;

public class StringDemo {
    public static void main(String args[]) {
        StringBuffer sBuffer = new StringBuffer("菜鸟教程网址：");
        sBuffer.append("www.");
        sBuffer.append("colby.");
        sBuffer.append("com");
        System.out.println(sBuffer+" "+String.valueOf(sBuffer.length()));

    }
}
