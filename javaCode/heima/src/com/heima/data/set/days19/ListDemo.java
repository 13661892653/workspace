package com.heima.data.set.days19;

import java.util.ArrayList;
import java.util.List;

import org.omg.PortableServer.ServantActivator;

public class ListDemo {
	public static void main(String[] args) {
		function01();
		function02();
	}

	public static void function01() {

		List<String> list = new ArrayList<>();
		list.add("abc");
		list.add("bde");
		list.add("etg");
		list.add("cty");
		System.out.println(list);
		list.add(0, "tta");
		System.out.println(list);

	}

	public static void function02() {

		List<Double> list = new ArrayList<Double>();
		list.add(1.11);
		list.add(1.12);
		list.add(1.13);
		list.add(1.14);
		System.out.println(list);
		Double d = list.remove(2);
		System.out.println(d);
		System.out.println(list);

	}
}
