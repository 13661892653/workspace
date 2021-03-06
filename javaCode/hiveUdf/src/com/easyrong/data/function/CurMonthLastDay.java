package com.easyrong.data.function;
import org.apache.hadoop.hive.ql.exec.UDF; 

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class CurMonthLastDay extends UDF{	
	public String evaluate(String s) throws ParseException {
        Calendar cal = Calendar.getInstance();
        cal.setTime(strToDate(s));
        cal.set(Calendar.DAY_OF_MONTH, 1);
        cal.add(Calendar.MONTH, 1);
        cal.add(Calendar.DATE, -1);
        //System.out.print(cal.add(Calendar.DATE, -1));
        String result=dateToStrLong(cal.getTime());
        return result;
    }
	public Date strToDate(String s) throws ParseException{
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
		Date date = sdf.parse(s);
		return date;
	}
	/** 
	 * 将长时间格式时间转换为字符串 yyyy-MM-dd
	 *  
	 * @param dateDate 
	 * @return 
	 */  
	public static String dateToStrLong(java.util.Date dateDate) {  
	    SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");  
	    String dateString = formatter.format(dateDate);  
	    return dateString;
	}	
}
