package com.easyrong.data.function;
import org.apache.hadoop.hive.ql.exec.UDF; 

public class HiveLower extends UDF{	
    public String evaluate(String s){  
        if (null == s){  
            return null;  
        }  
        return new String(s.toString().toLowerCase());  
    }  
    
    public static void main(String args[]){
    	HiveLower hiveLower= new HiveLower();
    	String result=hiveLower.evaluate("CHENLUN");
    	System.out.println(result);
    }
}
