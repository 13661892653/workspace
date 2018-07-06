package com.easyrong.data.days04;

public class SwitchDemo {
    public static void main(String args[]) {
        //switch后面跟表达式
        int week = 1;
        switch (week) {
            case 1:
                System.out.println("1");
                break;
            case 2:
                System.out.println("2");
                break;
            case 3:
                System.out.println("3");
                break;
            default:
                System.out.println("0");
                break;
        }

    }
}
