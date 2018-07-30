package com.heima.data.api.days15;

public class Exercise02 {
	public static void main(String[] args) {
		String str = "ddgaaBgGagah";
		exercise(str);
	}

	public static void exercise(String str) {
		String s = str.substring(0, 1);
		String e = str.substring(1);
		s = s.toUpperCase();
		e = e.toLowerCase();
		String result = s + e;
		System.out.println("结果：" + result);
	}

}
