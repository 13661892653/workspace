package com.easyrong.data.network.days32;

import java.net.InetAddress;
import java.net.UnknownHostException;

/*
 * java.net.InetAddress
 */
public class IP {
	public static void main(String[] args) throws UnknownHostException {
		InetAddress ip=InetAddress.getLocalHost();
		System.out.println(ip.getHostName().toString());//获取主机名
		System.out.println(ip.getHostAddress().toString());//获取IP地址
		System.out.println(InetAddress.getByName("127.0.0.1"));
	}
}
