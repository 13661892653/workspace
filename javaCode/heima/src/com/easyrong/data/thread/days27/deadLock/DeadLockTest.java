package com.easyrong.data.thread.days27.deadLock;

public class DeadLockTest{
	
	public static void main(String[] args) {
		DeadLock deadLock=new DeadLock();
		Thread t1=new Thread(deadLock);
		Thread t2=new Thread(deadLock);
		t1.start();
		t2.start();
	}
	
}
