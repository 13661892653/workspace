package com.easyrong.data.base.days11;

public class InterfaceTest {
    /*
     *接口中的常量可以直接用，无需实例化new:接口名.常量名
     */
    public static void main(String args[]){
        FirstInterfaceImp ff=new FirstInterfaceImp();
        ff.function();
        System.out.println(FirstInterface.a);
    }
}
