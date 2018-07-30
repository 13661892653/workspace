package com.heima.data.api.days15;

public class Exercise01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "QQ^&*co99lbyTGKH==`=00UUi0pQ!!";
		exercise(str);
	}

	public static void exercise(String str) {
		/**
		 * 数字：48-57 大写：65-90 小写：97-122
		 */
		int upper = 0;
		int lower = 0;
		int digit = 0;
		for (int i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			if (c >= 48 && c <= 57) {
				digit++;
			} else if (c >= 65 && c <= 90) {
				upper++;
			} else if (c >= 97 && c <= 122) {
				lower++;
			}
		}
		System.out.println("数字个数：" + digit);
		System.out.println("大写字母个数：" + upper);
		System.out.println("小写字母个数：" + lower);
	}
}
