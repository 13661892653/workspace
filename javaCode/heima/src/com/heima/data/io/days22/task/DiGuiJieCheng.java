package com.heima.data.io.days22.task;
/*
 * 递归求阶乘
 */
public class DiGuiJieCheng {
	public static void main(String[] args) {
		long sum=1;
		long initNum=10;
		long result=diGui(sum,initNum);
		System.out.println("计算结果为："+result);
	}
	
	public static long diGui(long sum,long n){
		//递归演示，最佳方法是for循环遍历
		sum=sum*n;
		System.out.println(sum+"   "+n);
		if(n==2){
			return sum;
		}
		return diGui(sum,n-1);	
	}
}
