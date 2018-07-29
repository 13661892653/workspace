package com.easyrong.data.network.days32.TCP;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	public static void main(String[] args) throws IOException {
		ServerSocket server=new ServerSocket(9999);
		Socket socket=server.accept();//获取客户端套接字对象
		//System.out.println(socket);
		InputStream in=socket.getInputStream();
		byte[] data=new byte[1024];
		int len=in.read(data);
		System.out.println( new String(data,0,len));
		//向客户端回送数据
		OutputStream out=socket.getOutputStream();
		out.write("亲，服务端已经收到您的消息啦！".getBytes());
		socket.close();
		server.close();
	}
}
