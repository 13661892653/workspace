package com.easyrong.data.exception.days21;
/**
 * @author colby
 *
 */

public class ThrowsDemo{
	public static void main(String args[]) throws Exception {
		function01();
	}
	
	public static void function01() throws Exception {
		int arr[]=new int[10];
		throw new Exception("内存溢出，异常测试！");//抛出异常
	}
}