package com.easyrong.data.thread.days26;

public class ThreadDemo {

	public static void main(String[] args) {
		Thread thread = Thread.currentThread();// 获得main的线程的名称的唯一方法
		System.out.println("当前线程名称：" + thread.getName());
		SubThread st = new SubThread();
		st.setName("colby的线程");
		st.start();
		SubThread st1 = new SubThread();
		st1.start();
		for (int i = 0; i <= 5; i++) {
			System.out.println("main..." + i);
		}
	}
}

/*
 * 多线程第一个案例
 */
class SubThread extends Thread {
	public void run() {
		System.out.println("当前线程的名称：" + getName());
		for (int i = 0; i <= 5; i++) {
			System.out.println("run..." + i);
		}
	}
}
