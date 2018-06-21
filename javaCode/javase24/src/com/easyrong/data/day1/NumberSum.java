package com.easyrong.data.day1;

import java.util.Scanner;

public class NumberSum {
    public static void main(String args[]){
        Scanner scanner=new Scanner(System.in);
        String number1=scanner.nextLine();
        String number2=scanner.nextLine();
        int n1 = Integer.parseInt(number1);
        int n2 = Integer.parseInt(number2);
        int jia = n1 + n2;
        int jian = n1 - n2;
        int cheng = n1 * n2;
        float chu = (float)n1 / n2;
        System.out.println(jia);
        System.out.println(jian);
        System.out.println(cheng);
        System.out.println(chu);

    }
}
