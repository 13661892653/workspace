package com.easyrong.data.days07_exercise;

public class Multiply99 {
    public static void main(String args[]){
        for(int row=1;row<=9;row++){
            for(int column=1;column<=row;column++){
                System.out.print(row+" * "+column+" = "+row*column+"  ");
            }
            System.out.println();
        }
    }
}
