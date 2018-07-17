package com.easyrong.data.set.days19;

import java.util.LinkedList;

public class LinkedListDemo {

	public static void main(String[] args) {
		function01();

	}

	/*
	 * addFirst(E)添加到链表的开头 addLast(E)添加到链表的结尾
	 */
	public static void function01() {

		LinkedList<String> link = new LinkedList<String>();
		link.add("a");
		link.add("b");
		link.add("c");
		link.add("d");

		System.out.println(link.getFirst());
		System.out.println(link.getLast());
		System.out.println(link.removeFirst());
		System.out.println(link.removeLast());
	}

}
