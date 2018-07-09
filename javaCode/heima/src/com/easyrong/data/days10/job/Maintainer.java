package com.easyrong.data.days10.job;

public abstract class Maintainer extends Employee{
    /*
     *
     */
    @Override
    public void work(){

        System.out.println("员工号为"+getId()+"的"+getName()+"员工，正在研发淘宝软件");

    }
}
