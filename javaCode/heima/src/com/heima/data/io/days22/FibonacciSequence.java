package com.heima.data.io.days22;
/*
 * 斐波那契数列的计算规则：F(n)=F(n-1)+F(n-2)
 * n>=2
 */
public class FibonacciSequence {

	public static void main(String[] args) {
		int i=F(12);
		System.out.println(i);
	}
	
	public static int  F(int n) {
		if(n==1) {
			return 1;
		}
		if(n==2) {
			return 1;
		}
		return F(n-1)+F(n-2);
	}
	
}
