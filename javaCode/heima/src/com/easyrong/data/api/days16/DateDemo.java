package com.easyrong.data.api.days16;

import java.text.SimpleDateFormat;
/*
 * 时间原点：公元1970-01-01 00:00:00，对应毫秒值：0
 */
import java.util.Date;

public class DateDemo {
	public static void main(String[] args) {
		Date date=new  Date();
		System.out.println("当前时间："+date);
		long time=System.currentTimeMillis();
		System.out.print("当前时间的毫秒值："+time);
				
	}
}
