package com.easyrong.data.set.days18;

import java.util.ArrayList;

import com.sun.org.apache.xml.internal.security.Init;

public class ArrayListDemo {

	public static void main(String[] args) {
		ArrayList<Integer> array=new ArrayList<Integer>();
		array.add(1);
		array.add(2);
		array.add(3);
		array.add(4);
		array.add(5);
		for(int i=0;i<array.size();i++) {
			System.out.println(array.get(i));
		}
	}
	
	

}
