package com.heima.data.udf;

import org.apache.hadoop.hive.ql.exec.UDF;

public class Upper extends UDF{
	
	public String evaluate(String s) {
		if (s==null) {
			return null;
		}
		return s.toUpperCase();	
	}
}
