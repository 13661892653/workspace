package com.easyrong.data.set.days19;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class HashSetDemo {
	public static void main(String[] args) {
		Set<String> set =new HashSet<String>();
		set.add("add");
		set.add("ggb");
		set.add("chh");
		set.add("colby");
		Iterator<String> it=set.iterator();	
		while(it.hasNext()) {
			System.out.println(it.next());
		}
	}
}
