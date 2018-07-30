package com.heima.data.thread.days26;

public class RunnableDemo {
	public static void main(String[] args) {
		SubRunnable sr=new SubRunnable();
		new Thread(sr).start();
		for(int i =0;i<5;i++) {
			System.out.println("main..."+i);
		}
	}
}
