package com.easyrong.data.thread.days26.task;

import java.util.concurrent.Callable;

public class CallableDemo implements Callable<Integer> {
	private int a;

	public CallableDemo(int a) {
		this.a = a;
	}

	public Integer call() {
		int sum = 0;
		for (int i = 1; i <= this.a; i++) {
			sum += i;
		}
		return sum;
	}
}
