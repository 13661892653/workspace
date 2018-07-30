package com.heima.data.io.days22;

import java.io.File;
import java.io.IOException;

public class FileDeno {
	public static void main(String[] args) throws IOException {
		//function01();
		createDir();
	}
	
	public static void function01() {
		File file=new File("e:","eclipse");
		System.out.println(file);
	}
	
	public static void createFile() throws IOException {
		File file=new File("E:\\project\\workspace\\javaCode\\heima\\src\\com\\easyrong\\data\\io\\days22\\createFile.txt");
		file.createNewFile();
	}
	
	public static void createDir() {
		File file=new File("E:\\\\project\\\\workspace\\\\javaCode\\\\heima\\\\src\\\\com\\\\easyrong\\\\data\\\\io\\\\days22\\\\dir");
		file.mkdirs();
	}
}
