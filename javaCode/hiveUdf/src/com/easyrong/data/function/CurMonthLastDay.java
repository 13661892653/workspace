package com.easyrong.data.function;
import org.apache.hadoop.hive.ql.exec.UDF; 
import org.apache.hadoop.io.Text;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class CurMonthLastDay extends UDF{	
	public String evaluate(String s) {
        Calendar cal = Calendar.getInstance();
        cal.setTime(strToDate(s));
        cal.set(Calendar.DAY_OF_MONTH, 1);
        cal.add(Calendar.MONTH, 1);
        cal.add(Calendar.DATE, -1);
        //System.out.print(cal.add(Calendar.DATE, -1));
        return cal.getTime();
    }
	public String strToDate(String s){
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
		Date date = sdf.parse(s);
		return date;
	}
	public static void main(String args[]) throws ParseException{
		
		CurMonthLastDay curMonthLastDay= new CurMonthLastDay();
		Date result = curMonthLastDay.evaluate(date);
		System.out.print(result);
	}
	
}