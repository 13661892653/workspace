package com.easyrong.data.function;
import org.apache.hadoop.hive.ql.exec.UDF; 

public class HiveUpper extends UDF{	
    public String evaluate(String s){  
        if (null == s){  
            return null;  
        }  
        return new String(s.toString().toUpperCase());  
    } 
    
    public static void main(String args[]){
    	HiveUpper hveUpper= new HiveUpper();
    	String result=hveUpper.evaluate("chenlun");
    	System.out.println(result);
    }
}
