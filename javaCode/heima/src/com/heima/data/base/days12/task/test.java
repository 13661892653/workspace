package com.heima.data.base.days12.task;

public class test {
    public static void main(String args[]) {
        /*
         *
         * */
        Student s=new Student("colby",20);
        Worker w=new Worker("bobby",30);
        System.out.println(s.getClass()+"\n"+s.getAge()+" "+s.getName());
        System.out.println(w.getClass()+"\n"+w.getAge()+" "+w.getName());

    }
}
