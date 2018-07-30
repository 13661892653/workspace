package com.heima.data.set.days20;

public class VarArgumentsDemo {
	public static void main(String[] args) {
		getSum("a","b");
	}
	
	public static void getSum(String...a) {
		for(int i=0;i<a.length;i++) {
			System.out.println(a[i]);
		}
	}
}
