package com.heima.data.base.days11;

public class FirstInterfaceImp implements FirstInterface {
    /*
     *
     */

    @Override
    public void function() {
//      重写接口中的方法必须写public权限
//      实现类，实现接口必须重写接口中的全部抽象方法
        System.out.println("FirstInterfaceImp类实现了接口FirstInterface。");
    }
}
