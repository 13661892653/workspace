package com.easyrong.data.io.days22;

import java.io.File;
import java.io.FileFilter;

public class GetFileAll {
	public static void main(String[] args) {
		File dir=new File("E:\\project\\workspace\\javaCode\\heima\\src");
		getFileAll(dir);
	}
	
	//实现目录的全遍历
	public static void getFileAll(File dir) {
		System.out.println("目录==>："+dir);
		File[] files=dir.listFiles(new FileFilter() {
			public boolean accept(File pathname) {
				return true;
			}
		});//匿名函数FileFilter
		for (File file : files) {
			if (file.isDirectory()) {
				//遍历文件夹
				getFileAll(file);
			} else {
				System.out.println("文件："+file);
			}
		}
	}
	
}
