package com.heima.data.io.days23;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamDemo {
	public static void main(String[] args) {
		try {
			funtion01();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void funtion01() throws IOException {
		File file=new File("E:\\a.txt");
		FileOutputStream fos= new FileOutputStream(file,true);//true代表追加
		fos.write("ddd".getBytes());
		fos.write("ddd".getBytes());
		fos.close();
	}
}
