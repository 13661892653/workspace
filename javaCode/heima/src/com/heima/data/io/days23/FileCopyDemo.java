package com.heima.data.io.days23;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/*
 * 将数据源复制到目标路径下
 * A-->B
 * 
 */
public class FileCopyDemo {
	public static void main(String[] args) {	
		copyFile();
	}
	
	public static void copyFile() {
		File fromFile=new File("E:\\testlog\\access.log");
		File toFile=new File("D:\\project\\workspace\\javaCode\\heima\\src\\com\\easyrong\\data\\io\\days23\\access.log");
		FileInputStream fis=null;
		FileOutputStream fos=null;
		try {
			fis=new FileInputStream(fromFile);
			fos=new FileOutputStream(toFile);
			byte[] bytes=new byte[1024];
			int len=0;
			while((len=fis.read(bytes))!=-1) {
				fos.write(bytes, 0, len);
			}
		} catch (Exception e) {
			System.out.println(e);
			throw new RuntimeException("文件复制中断");
		} finally {			
			try {
				if(fos!=null)
				fos.close();
			} catch (IOException e) {
				e.printStackTrace();
			}finally {
				try {
					if(fis!=null)
					fis.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
}
