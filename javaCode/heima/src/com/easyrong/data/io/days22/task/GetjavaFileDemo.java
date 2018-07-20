package com.easyrong.data.io.days22.task;

import java.io.File;

public class GetjavaFileDemo {
	public static void main(String args[]) {
		File pathName = new File("E:\\project\\workspace");
		getJavaFile(pathName);
	}

	public static void getJavaFile(File pathname) {
		File[] files = pathname.listFiles(new MyJavaFileter());
		for (File file : files) {
			if (file.isDirectory()) {
				getJavaFile(file);
			} else {
				System.out.println(file);
			}
		}
	}

}
