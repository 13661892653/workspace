package com.heima.data.network.days32.UDPonceSend;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
/*
 * DatagramPacket 消息打包类
 * DatagramSocket 消息发送类
 * 
 */
public class UDPSendDemo {
	public static void main(String[] args) throws IOException {
		byte[] data="亲，您好！".getBytes();
		InetAddress inet=InetAddress.getByName("127.0.00.1");
		DatagramPacket dg=new DatagramPacket(data, data.length,inet,5000);
		DatagramSocket dsend=new DatagramSocket();
		dsend.send(dg);
		dsend.close();
	}
}
