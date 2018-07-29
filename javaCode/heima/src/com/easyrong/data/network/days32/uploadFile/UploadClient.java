package com.easyrong.data.network.days32.uploadFile;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class UploadClient {
	public static void main(String[] args) throws IOException {
		Socket socket = new Socket("127.0.0.1", 9999);
		// 获取字节输出流，图片写入服务器
		OutputStream out = socket.getOutputStream();
		FileInputStream local_in = new FileInputStream("C:\\Users\\Administrator\\Desktop\\微信图片_20180520141724.jpg");
		int len = 0;
		byte[] data = new byte[1024];
		while ((len = local_in.read(data)) != -1) {
			out.write(data, 0, len);
		}
		// 告诉服务器数据传输完了，别傻等了
		socket.shutdownOutput();
		// 获取字节输入流
		InputStream in = socket.getInputStream();
		len = in.read(data);
		System.out.println(new String(data, 0, len));
		local_in.close();
		out.close();
		in.close();
	}
}
