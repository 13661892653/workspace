package com.easyrong.data.network.days32.TCP;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

/*
 * OutputStream输出到服务到
 * InputStream接受服务端的数据
 * Server端的流也是一样
 * client的OutputStream对应服务端的InputStream
 * client的InputStream对应服务端的OutputStream
 */
public class Client {
	public static void main(String[] args) throws IOException {
		Socket clent= new Socket("127.0.0.1",9999);
		OutputStream out=clent.getOutputStream();
		out.write("发送的第一条信息".getBytes());
		InputStream in=clent.getInputStream();
		byte[] data=new byte[1024];
		int len=in.read(data);
		System.out.println( new String(data,0,len));
		out.close();		
	}
}
