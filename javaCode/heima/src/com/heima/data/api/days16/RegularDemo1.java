package com.heima.data.api.days16;

/*
 * "abc".matches(String 正则规则) 匹配成功返回true
 * 
 * "abc".split(String 正则规则) 使用规则将字符串进行切割
 * 
 * "abc113".replaceAll(前面是规则，"替换成的字符")
 * 
 */

public class RegularDemo1 {
	public static void main(String[] args) {
		String QQNumber = "470563152661";
		checkPhoneNumber(QQNumber);
		
		String spiltStr="08-17-344-723-3";
		splitString(spiltStr);
		
		String replaceStr="agagaga136945hahaha789dfada";
		replaceAllDemo(replaceStr);
		
	}

	public static void checkPhoneNumber(String QQNumber) {
		/**
		 * 检查QQ号是否满足需求： 5到11位 全是数字 首位不能为0
		 */
		String Pattern = "[1-9][0-9]{4,10}";
		boolean result = QQNumber.matches(Pattern);
		System.out.println(QQNumber + "是否为合法QQ号码呢？" + result);
		
	}
	
	public static void splitString(String s) {
		/**
		 * 字符串分割
		 */
		String[] result=s.split("-");
		for(int i=0; i<result.length;i++) {
			System.out.println(result[i]);
		}
	}
	
	public static void replaceAllDemo(String s) {
		/**
		 * 字符串替换
		 */
		String result=s.replaceAll("[\\d]+", "#");
		System.out.println(result);
	}
}
