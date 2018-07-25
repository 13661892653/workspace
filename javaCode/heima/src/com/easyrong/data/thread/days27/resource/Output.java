package com.easyrong.data.thread.days27.resource;

public class Output implements Runnable {

	private Resource r;

	public Output(Resource r) {
		this.r = r;
	}

	public void run() {
		while (true) {
			synchronized (r) {
				if (!r.flag) {
					try {
						r.wait();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
				System.out.println(r.name + "..." + r.sex);
				r.flag = false;
				r.notify();
			}

		}
	}
}
