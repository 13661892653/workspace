package com.easyrong.data.io.days24.buffered;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FilterInputStream;
import java.io.IOException;


public class BufferedStreamCopyFile {

	public static void main(String[] args) throws IOException{
		long start=System.currentTimeMillis();
		copyFile();
		long end=System.currentTimeMillis();
		System.out.println("拷贝花费时间："+(end-start));
	}

	public static void copyFile() throws IOException{
		File fromFile=new File("F:\\BaiduNetdiskDownload\\Oracle10g_client_win32 .zip");
		File toFile=new File("D:\\testJava\\Buffered\\Oracle10g_client_win32 .zip");
		FileInputStream fis=new FileInputStream(fromFile);
		FileOutputStream fos=new FileOutputStream(toFile);
		BufferedInputStream bis=new BufferedInputStream(fis);
		BufferedOutputStream bos=new BufferedOutputStream(fos);
		int len=0;
		byte[] bytes=new byte[1024*10];
		while((len=bis.read(bytes))!=-1) {
			bos.write(bytes,0,len);
		}
		bis.close();
		bos.close();
	}
}
