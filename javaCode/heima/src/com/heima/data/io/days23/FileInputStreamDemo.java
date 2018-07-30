package com.heima.data.io.days23;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class FileInputStreamDemo {
	public static void main(String[] args) throws IOException {
			function01();
	}
	
	public static void function01()  throws IOException {
		File file=new  File("C:\\kms10.log");
		FileInputStream fis=new FileInputStream(file);
		int len=0;
		while ((len=fis.read())!=-1) {
			System.out.print((char)len);
		}	
		fis.close();
	}
}
