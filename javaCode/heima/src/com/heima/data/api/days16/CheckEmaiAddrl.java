package com.heima.data.api.days16;

public class CheckEmaiAddrl {
	public static void main(String[] args) {
		String emailAddr = "colby@126.com";
		checkMail(emailAddr);
	}

	public static void checkMail(String emailAddr) {
		String regex = "[0-9a-zA-Z_]+@[0-9a-zA-Z_]+\\.[0-9a-z_A-Z]+";
		boolean result = emailAddr.matches(regex);
		System.out.println(emailAddr + "格式是否合法：" + result);
	}

}
