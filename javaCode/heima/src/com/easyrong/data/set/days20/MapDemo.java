package com.easyrong.data.set.days20;

import java.util.HashMap;
import java.util.Map;

/*
 * Map接口中的常用方法
 * 使用Map接口的实现类的HashMap
 * Map有返回值，插入重复键时返回的是被覆盖之前的值，其他情况返回null值
 */
public class MapDemo {
	public static void main(String[] args) {
		function();
	}
	
	public static void function() {
		Map<String,Integer> map=new HashMap<String,Integer>();
		map.put("colby", 10);
		map.put("cl", 20);
		map.put("pll", 30);
		map.put("pll", 50);
		System.out.println(map.get("pll"));
		for(String key:map.keySet()) {
			System.out.println(key+":"+map.get(key));
		}
		
	}
	
}
