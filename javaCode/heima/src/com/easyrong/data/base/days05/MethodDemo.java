package com.easyrong.data.base.days05;

public class MethodDemo {
    public static void main(String args[]) {
        //局部变量
        //类变量（静态变量）
        //成员变量（非静态变量）
        int b = getArea(6, 888);
        System.out.print("长方形的面积：" + b);
    }

    public static float getArea(float length, float width) {
        return length * width;
    }

    public static int getArea(int length, int width) {
        return length * width;
    }

    public static double getArea(double length, double width) {
        return length * width;
    }

}
