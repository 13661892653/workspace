package com.easyrong.data.base.days14;

/**
 * 
 * @author chenlun
 *
 *         计算面积跟边长
 * 
 * 
 */

public class CFX {
	private int w;
	private int h;

	public CFX(int w, int h) {
		this.w = w;
		this.h = h;
	}

	public double r() {
		return (w + h) * 2;
	}

	public double s() {
		return (w * h);
	}

	public int getW() {
		return this.w;
	}

	public void setW(int w) {
		this.w = w;
	}

	public int getH() {
		return this.h;
	}

	public void setH(int h) {
		this.h = h;
	}

}
