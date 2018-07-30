package com.heima.data.api.days16.task;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Exercise01 {

	public static void main(String[] args) throws ParseException {
		// 计算一下自己活了多少天了
		//生日是哪天？今天是几号
		//毫秒值相减
		calc();
		
	}
	
	public static void calc() throws ParseException {
		System.out.println("请输入您的出生日期（YYYY-MM-DD）：");
		Scanner scanner=new Scanner(System.in);
		String birthday=scanner.next();
		SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd");
		Date birthdayDate=sdf.parse(birthday);
		Date today=new Date();
		long birthdaySecond=birthdayDate.getTime();
		long todaySecond=today.getTime();
		double second=todaySecond-birthdaySecond;
		double days=second/1000/3600/24;
		System.out.println("days:"+days);
		if (days<0) {
			System.out.println("您还有"+Math.abs(days)+"天出生！");
		}else {
			System.out.println("您已经活了"+days+"天了！");
		}
		
	}

}
