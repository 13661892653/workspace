package com.easyrong.data.network.days32.uploadFile;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;


public class UploadServer {
	public static void main(String[] args) throws IOException {
		ServerSocket server=new ServerSocket(9999);
		Socket client=server.accept();
		
		InputStream in=client.getInputStream();
		File upload=new File("D:\\testJava\\upload");
		if(!upload.exists()) {
			upload.mkdirs();
		}
		//防止文件名重复，定义文件生成规则
		//域名+毫秒数+6位随机数
		String filename="colby"+System.currentTimeMillis()+new Random().nextInt(999999)+".jpg";
		FileOutputStream local_out=new FileOutputStream(upload+File.separator+filename);
		byte[] data=new byte[1024];	
		int len=0;
		while((len=in.read(data))!=-1) {
			local_out.write(data,0,len);
		}
		//通过客户端对象，上传成功信息传回客户端		
		client.getOutputStream().write("上传成功啦".getBytes());
		local_out.close();
		client.close();
		server.close();
	}
}
