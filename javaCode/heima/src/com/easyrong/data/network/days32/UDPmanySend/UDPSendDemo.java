package com.easyrong.data.network.days32.UDPmanySend;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;
/*
 * DatagramPacket 消息打包类
 * DatagramSocket 消息发送类
 * 
 */
public class UDPSendDemo {
	public static void main(String[] args) throws IOException {
		while(true) {
			Scanner scan=new Scanner(System.in);
			String content=scan.nextLine();
			byte[] data=content.getBytes();
			InetAddress inet=InetAddress.getByName("127.0.00.1");
			DatagramPacket dg=new DatagramPacket(data, data.length,inet,5000);
			DatagramSocket dsend=new DatagramSocket();
			dsend.send(dg);
			dsend.close();		
		}
	}
}
