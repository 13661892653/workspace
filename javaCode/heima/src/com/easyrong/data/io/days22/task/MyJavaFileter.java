package com.easyrong.data.io.days22.task;

import java.io.File;
import java.io.FileFilter;

public class MyJavaFileter implements FileFilter {

	@Override
	public boolean accept(File pathname) {
		if(pathname.isFile()) {
			return pathname.getName().endsWith(".class");
		}
		return true;
	}

}
