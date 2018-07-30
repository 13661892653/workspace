package com.heima.data.api.days15;



public class StringDemo {
	
	
	public static void main(String[] args) {
		
		String str="colby";
		System.out.println("字符串长度："+str.length()+" "+str.hashCode());
		System.out.println("字符串长度："+str.toUpperCase());
		byte bytes[]= {65,66,67,68,69};
		//offset数组的起始位置
		String s1=new String(bytes);
		String s2=new String(bytes,0,5);
		System.out.println("字符串输出："+s1+"\n字符串截取："+s2);	
		
	}
		
}
