package com.easyrong.data.api.days17;

public class PerfectNumber {
	public static void main(String[] args) {
		for (int i = 2; i < 10000000; i++) {
			int sum = 0;
//查找因数
			for (int j = 1; j < i; j++) {
				if (i % j == 0) {
					sum += j;
				}
				if (sum == i)
					System.out.println(i);
			}
		}
	}
}
