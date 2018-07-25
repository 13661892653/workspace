package com.easyrong.data.thread.days27;

import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Lock;

public class RunnableDemo implements Runnable {
	private int tickt = 100;
	private Lock lock = new ReentrantLock();

	public void run() {
		while (true) {
			lock.lock();
			if (tickt > 0) {
				try {
					Thread.sleep(10);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				System.out.println(Thread.currentThread().getName() + "正在出售：" + (tickt--));
			}
			lock.lock();
		}
	}
}
