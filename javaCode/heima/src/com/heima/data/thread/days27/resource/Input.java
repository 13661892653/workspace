package com.heima.data.thread.days27.resource;

public class Input implements Runnable {
	private Resource r;

	public Input(Resource r) {
		this.r = r;
	}

	public void run() {
		int i = 0;
		while (true) {
			synchronized (r) {
				if (r.flag) {
					try {
						r.wait();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}

				if (i % 2 == 0) {
					r.name = "陈";
					r.sex = "男";
				} else {
					r.name = "colby";
					r.sex = "女";
				}

				r.flag = true;
				r.notify();
			}
			i++;
		}
	}
}
