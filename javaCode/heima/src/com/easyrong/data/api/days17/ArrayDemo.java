package com.easyrong.data.api.days17;

import java.util.Arrays;

import com.sun.org.apache.xml.internal.security.Init;

public class ArrayDemo {
	public static void main(String[] args) {
		int[] arr= {1,6,3,9,11,78,0};
		Arrays.sort(arr);
		String res=Arrays.toString(arr);
		System.out.println(res);		
	}
}
