package com.runoob.base;


// 一个简单的构造函数
class MyClass {
    int x;

    // 以下是构造函数
    MyClass(int i ) {
        x = i;
    }
}

public class ConstractMethod {
    //static void printMax( double... numbers)
    //可变参数
    public static void main(String args[]) {
        MyClass t1 = new MyClass( 10 );
        MyClass t2 = new MyClass( 20 );
        System.out.println(t1.x + " " + t2.x);
    }
}

