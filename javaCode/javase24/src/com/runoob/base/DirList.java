package com.runoob.base;

import java.io.File;

public class DirList {
    public static void main(String args[]) {
        String dirname="E:\\workspace";
        File f=new File(dirname);
        if (f.isDirectory()){
            System.out.println("目录："+dirname);
            String s[]=f.list();
            for(int i=0;i<s.length;i++){
                File file1=new File(dirname+"/"+s[i]);
                if (f.isDirectory()){
                    System.out.println("'"+file1+"' 是一个目录");
                } else {
                    System.out.println("'"+file1+"' 是一个文件");
                }
            }
        } else {
            System.out.println(dirname+"不是一个目录");
        }

    }
}
