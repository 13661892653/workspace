package com.easyrong.data.io.days23;

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
		FileOutputStream fos= new FileOutputStream("E:\\tmp\\a.txt");
		fos.write("我的名字叫colby".getBytes());
		fos.close();
	}
}
