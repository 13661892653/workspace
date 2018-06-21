package com.easyrong.data.day1;

import java.util.Scanner;

/**
 *
 */
public class LogicProcess {

    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        String name = scn.nextLine();
        if(name.equals("tom")) {
            System.out.println("欢迎你," + name);
        }else if(name.equals("jim")) {
            System.out.println("您好," + name);
        }else{
            System.out.println("滚蛋," + name);

        }
    }
}
