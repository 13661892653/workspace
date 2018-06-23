package com.easyrong.data.homework;

import java.util.Scanner;

public class GuessNumber {
    public static void main(String args[]) {
        int num = 9;
        while (true) {
            Scanner scanner = new Scanner(System.in);
            String rec = scanner.nextLine();
            int userguess = Integer.parseInt(rec);
            if (userguess > num) {
                System.out.println("您猜的太大了！");
            } else if (userguess < num) {
                System.out.println("您猜的太小了！");
            } else {
                System.out.println("恭喜你答对了！");
                break;
            }
        }

    }
}
