package com.heima.data.set.days20;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class EntrySetDemo {
	public static void main(String[] args) {
		Map<String,Integer> map=new HashMap<String,Integer>();
		map.put("colby", 10);
		map.put("cl", 20);
		map.put("pll", 30);
		map.put("pll", 50);
		Set<Map.Entry<String, Integer>> set=map.entrySet();
		System.out.println(set);
	}
}
