package com.easyrong.data.thread.days27;

public class RunnableDemo implements Runnable {

	private int tickt = 100;
	private Object obj = new Object();

	public void run() {
		while (true) {
			synchronized (obj) {
				if (tickt > 0) {
					try {
						Thread.sleep(10);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					System.out.println(Thread.currentThread().getName() + "正在出售：" + (tickt--));
				}
			}
		}
	}
}
