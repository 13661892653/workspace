package com.easyrong.data.thread.days26;

public class SubRunnable implements Runnable{
	public void run() {
		for(int i =0;i<5;i++) {
			System.out.println(Thread.currentThread().getName()+" run..."+i);
		}	
	}
}
