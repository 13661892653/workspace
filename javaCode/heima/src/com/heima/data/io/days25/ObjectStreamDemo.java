package com.heima.data.io.days25;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class ObjectStreamDemo {
	public static void main(String[] args)  throws IOException, ClassNotFoundException{
		objectOutputStream();
		objectIntputStream();
	}	
	/*
	 * ObjectOutputStream(OutputStream out)
	 * 传递任意的字节输出流
	 * void writeObject()写出对象的方法
	 */
	public static void objectOutputStream() throws IOException{
		Person p1=new Person("colby", 20);
		FileOutputStream fos=new FileOutputStream("e:\\testjava\\OutputStream.txt");
		ObjectOutputStream oos=new ObjectOutputStream(fos);
		oos.writeObject(p1);
		oos.close();
	}
	
	public static void objectIntputStream() throws IOException, ClassNotFoundException{
		FileInputStream fis=new FileInputStream("e:\\testjava\\OutputStream.txt");
		ObjectInputStream ois=new ObjectInputStream(fis);
		Object obj=ois.readObject();
		System.out.println(obj);
		ois.close();
	}
}
