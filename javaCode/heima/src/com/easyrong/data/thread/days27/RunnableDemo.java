package com.easyrong.data.thread.days27;

public class RunnableDemo implements Runnable {

	private int tickt = 100;
	public synchronized void run() {
		while (true) {
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
