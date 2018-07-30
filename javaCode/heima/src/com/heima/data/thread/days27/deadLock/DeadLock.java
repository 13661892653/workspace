package com.heima.data.thread.days27.deadLock;

public class DeadLock implements Runnable{
	private int i=0;
	public void run() {
		while(true) {
			if(i%2==0) {
				synchronized (MyLock.LockA) {
					System.out.println("if...LockA");
					synchronized (MyLock.LockB) {
						System.out.println("if...LockB");
					}
				}
			}else {
				synchronized (MyLock.LockB) {
					System.out.println("else...LockB");
					synchronized (MyLock.LockA) {
						System.out.println("else...LockA");
					}
				}
			}
			i++;
		}
	}
}
