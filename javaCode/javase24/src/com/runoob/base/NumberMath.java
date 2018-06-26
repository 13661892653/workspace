package com.runoob.base;

public class NumberMath {
    public static void main(String args[]){
        //所有的包装类(Integer、Long、Byte、Double、Float、Short)
        // 都是抽象类 Number 的子类。
        System.out.println("90 度的正弦值：" + Math.sin(Math.PI/2));
        System.out.println("0度的余弦值：" + Math.cos(0));
        System.out.println("60度的正切值：" + Math.tan(Math.PI/3));
        System.out.println("1的反正切值： " + Math.atan(1));
        System.out.println("π/2的角度值：" + Math.toDegrees(Math.PI/2));
        System.out.println(Math.PI);
        System.out.println("-100绝对值："+Math.abs(-100));
    }
}
