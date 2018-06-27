package com.runoob.base;

public class Method {
    public static void main(String args[]) {
        //修饰符 返回值类型 方法名(参数类型 参数名){
        //    ...
        //    方法体
        //    ...
        //    return 返回值;
        //}
        int result=max(6,1);
        System.out.println(result);

    }

    //void没有返回值，括号内为输入参数public后面紧跟的是返回值的类型
    public static int max(int num1, int num2) {
        int result;
        if (num1 > num2)
            result = num1;
        else
            result = num2;
        return result;
    }

}