package com.heima.data.thread.days27;

public class GetTickt {

	public static void main(String[] args) {
		RunnableDemo ticket = new RunnableDemo();
		Thread t0 = new Thread(ticket);
		Thread t1 = new Thread(ticket);
		Thread t2 = new Thread(ticket);
		t0.start();
		t1.start();
		t2.start();
	}

}
