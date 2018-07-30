package com.heima.data.io.days24;
/*
 * 转换流+字符集
 */
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class OutputStreamWriterDemo {
	public static void main(String[] args) throws IOException {
		writeGBK();
		writeUTF8();
	}
	
	public static void writeGBK() throws IOException {
		File fromFile=new File("D:\\testJava\\Hadoop-2.9.txt");
		File toFile  =new File("D:\\testJava\\Hadoop-2.9_copyGBK.txt");
		FileInputStream fis=new FileInputStream(fromFile);
		FileOutputStream fos=new FileOutputStream(toFile);
		InputStreamReader isr=new InputStreamReader(fis,"UTF-8");
		OutputStreamWriter osw=new OutputStreamWriter(fos,"GBK");
		int len=0;
		char[] chars=new char[1024];
		while((len=isr.read(chars))!=-1) {
			osw.write(chars, 0, len);
		}
		isr.close();
		osw.close();
	}
	
	public static void writeUTF8() throws IOException{
		File fromFile=new File("D:\\testJava\\Hadoop-2.9_copyUTF8.txt");
		File toFile  =new File("D:\\testJava\\ERROR.txt");
		FileInputStream fis=new FileInputStream(fromFile);
		FileOutputStream fos=new FileOutputStream(toFile);
		InputStreamReader isr=new InputStreamReader(fis,"UTF8");
		OutputStreamWriter osw=new OutputStreamWriter(fos,"gbk");
		int len=0;
		char[] chars=new char[1024];
		while((len=isr.read(chars))!=-1) {
			osw.write(chars, 0, len);
		}
		isr.close();
		osw.close();
	}
}
