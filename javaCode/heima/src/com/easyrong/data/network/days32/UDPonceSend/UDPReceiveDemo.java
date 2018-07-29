package com.easyrong.data.network.days32.UDPonceSend;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;


public class UDPReceiveDemo {

	public static void main(String[] args) throws IOException {
		byte[] data=new byte[1024];
		DatagramSocket receive=new DatagramSocket(5000);
		DatagramPacket dp=new DatagramPacket(data,data.length);
		receive.receive(dp);
		int len=dp.getLength();
		int port=dp.getPort();
		String ip=dp.getAddress().getHostAddress();
		System.out.println("发送主机："+ip+" 端口："+port+new String(data,0,len));
		receive.close();
	}

}
