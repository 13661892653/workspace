package com.heima.data.thread.days27.resource;

public class ResourceTest {
	public static void main(String[] args) {
		Resource r=new Resource();
		Thread t1=new Thread(new Input(r));
		Thread t2=new Thread(new Output(r));
		t1.start();
		t2.start();
	}
}
