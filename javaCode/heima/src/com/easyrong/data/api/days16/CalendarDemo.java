package com.easyrong.data.api.days16;

import java.util.Calendar;

/*
 * 日历类
 * 不需要直接New子类调用，通过getInstance静态方法调用
 */
public class CalendarDemo {
	public static void main(String[] args) {
		Calendar cl = Calendar.getInstance();
		System.out.println(cl.get(Calendar.DAY_OF_YEAR));
	}
}
