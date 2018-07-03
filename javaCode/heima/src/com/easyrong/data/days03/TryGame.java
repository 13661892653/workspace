package com.easyrong.data.days03;

import java.util.Random;
import java.util.Scanner;

/*
    switch表达式数据类型
    JDK1.0-1.4 数据类型接受byte short int char
    JDK1.5-1.6 数据类型接受byte short int char enum(枚举)
    JDK1.7 数据类型接受byte short int char enum(枚举) String
*/
public class TryGame {
    public static void main(String args[]) {
        Random ran=new Random();
        int num=ran.nextInt(100);
        System.out.println("猜数字游戏开始了！");
        System.out.println("请输入数字：");
        while(true){

            Scanner s=new Scanner(System.in);
            int inputNum=s.nextInt();
            if(inputNum==num){
                System.out.println("恭喜您，猜对了");
                break;
            }else if(inputNum>num){
                System.out.println("Sorry,您猜大了");
            }
            else{
                System.out.println("Sorry,您猜小了");
            }

        }

    }
}
