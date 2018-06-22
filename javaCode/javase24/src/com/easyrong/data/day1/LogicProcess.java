package com.easyrong.data.day1;

import java.util.Scanner;

/**
 *
 */
public class LogicProcess {

    public static void main(String args[]) {
        int count=10;
        int i=0;
        while(i<=count){
            Scanner scn = new Scanner(System.in);
            String name = scn.nextLine();
            if(name.equals("tom")) {
                System.out.println("welcome," + name);
            }else if(name.equals("jim")) {
                System.out.println("Hi," + name);
            }else{
                System.out.println("fuck off," + name);

            }
            i++;
        }

    }
}
