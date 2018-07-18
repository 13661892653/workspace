package com.easyrong.data.exception.days21;

public class ExceptionDemo extends Object{
	public static void main(String[] args) {
		int arr[]= {};
		try {
			int i=function01(arr);
			System.out.println(i);
			System.out.println("Game Over!");
		}catch (ArrayIndexOutOfBoundsException e) {
			System.out.println(e);
		}finally {
			System.out.println("异常处理完毕");
		}
	}
	
	public static int function01(int[] arr){
		return arr[3]+1;		
	}
}
