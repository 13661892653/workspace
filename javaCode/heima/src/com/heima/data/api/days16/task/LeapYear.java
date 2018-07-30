package com.heima.data.api.days16.task;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import com.heima.data.base.days06.DianFanGuo;

public class LeapYear {

	public static void main(String[] args) throws ParseException {
		// 闰年的计算
		leapYear("2001-01-01");
	}

	public static void leapYear(String date) throws ParseException {
		//获取日期，转换成Date类型
		Date sdf = new SimpleDateFormat("yyyy-MM-dd").parse(date);
		Calendar c = Calendar.getInstance();
		//设置传入的日期为日历时间
		c.setTime(sdf);
		//获取年份
		int year = c.get(Calendar.YEAR);
		//将日历时间设置成当年3月1号
		c.set(year, 2, 1);
		//3月1号减1天
		c.add(Calendar.DAY_OF_MONTH, -1);
		//获取2月的天数
		int days = c.get(Calendar.DAY_OF_MONTH);
		if (days == 29) {
			System.out.println("闰年：" + days);
		} else {
			System.out.println("平年：" + days);
		}
	}
}
