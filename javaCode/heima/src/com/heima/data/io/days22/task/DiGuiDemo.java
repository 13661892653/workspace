package com.heima.data.io.days22.task;
/*
 * 递归求和
 */
public class DiGuiDemo {
	public static void main(String[] args) {
		int sum=0;
		int initNum=100;
		int result=diGui(sum,initNum);
		System.out.println("计算结果为："+result);
	}
	
	public static int diGui(int sum,int n){
		//递归演示，最佳方法是for循环遍历
		sum=sum+n;
		if(n==1){
			return sum;
		}
		return diGui(sum,n-1);	
	}
}
