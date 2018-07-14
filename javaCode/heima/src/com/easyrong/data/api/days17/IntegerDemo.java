package com.easyrong.data.api.days17;

public class IntegerDemo {
	public static void main(String[] args) {
		long start=System.currentTimeMillis();
		int a=Integer.parseInt("2000");
		System.out.println(a);
		
		int b=Integer.parseInt("110",2);//指定进制，输出10进制
		System.out.println(b);
		System.currentTimeMillis();
		System.out.println(System.getProperties());;
		for(int j=0;j<10000;j++) {
			for(int i=0;i<10;i++) {
				System.out.println(i);
			}
		}
		long end=System.currentTimeMillis();
		System.out.println(end-start);
	}
}
