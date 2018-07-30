package com.heima.data.api.days15;

public class StringOtherDemo {
	public static void main(String[] args) {
		strExper();
		subString(0,8);
	}
	
	public static void strExper(){
		String str="ABCabc&&#$%";
		int len=str.length();
		System.out.println("字符串的长度："+len);
	}
	
	public static void subString(int s,int e) {
		String str="ABCabc&&#$%";
		String result=str.substring(s, e);
		System.out.println(result);
	}
}
