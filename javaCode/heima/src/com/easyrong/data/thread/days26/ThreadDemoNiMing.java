package com.easyrong.data.thread.days26;

public class ThreadDemoNiMing {
	public static void main(String[] args) {
		new Thread() {
			public void run() {
				System.out.println("Thread匿名内部类实现多线程！");
			}
		}.start();
			
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				System.out.println("Runnable匿名内部类实现多线程！");				
			}
		}).start();
	}
}
