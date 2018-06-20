package com.easyrong.data.day1;

import java.util.Scanner;

public class NumberSum {
    public static void main(String args[]){
        Scanner scanner=new Scanner(System.in);
        String number1=scanner.nextLine();
        String number2=scanner.nextLine();
        int res=Integer.parseInt(number1) + Integer.parseInt(number2);
        System.out.println(res);

    }
}
