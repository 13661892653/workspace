package com.easyrong.data.api.days16;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateFormatDemo {
	public static void main(String[] args) throws ParseException {
		//时间格式化
		Date date=new Date();
		SimpleDateFormat sdf1=new SimpleDateFormat("yyyy年MM月dd日 HH时mm分ss秒SS毫秒");
		String result=sdf1.format(date);
		System.out.println(result);
		//parse方法，将字符串解析为日期对象
		//不建议手工输入，采用选择的方式供用户选择
		SimpleDateFormat sdf2=new SimpleDateFormat("yyyy-MM-dd");
		Date date2=sdf2.parse("2018-1-1");
		System.out.println(date2);
	}
}
