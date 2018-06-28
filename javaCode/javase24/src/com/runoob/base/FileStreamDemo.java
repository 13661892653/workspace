package com.runoob.base;

import java.io.*;

public class FileStreamDemo {
    public static void main(String args[]) throws Exception {
        //局部变量
        //类变量（静态变量）
        //成员变量（非静态变量）
        File file =new File("FileStreamDemo.txt");
        FileOutputStream fos=new FileOutputStream(file);
        OutputStreamWriter writer=new OutputStreamWriter(fos,"UTF-8");
        writer.append("我的中文名叫陈先生");
        writer.append("\r\n");
        writer.append("My name is Mr.chen");
        //关闭写入流,同时会把缓冲区内容写入文件,所以上面的注释掉
        writer.close();
        // 关闭输出流,释放系统资源
        fos.close();


        FileInputStream fip=new FileInputStream(file);
        InputStreamReader reader=new InputStreamReader(fip,"UTF-8");

        StringBuffer strBuff = new StringBuffer();
        while (reader.ready()){
            strBuff.append((char) reader.read());
        }

        System.out.println(strBuff.toString());
        reader.close();
        // 关闭读取流

        fip.close();
        // 关闭输入流,释放系统资源
    }
}
