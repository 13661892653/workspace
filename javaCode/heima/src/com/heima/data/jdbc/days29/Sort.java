package com.heima.data.jdbc.days29;

public class Sort {
	private int sid;
	private String sname;
	private double sprice;
	private String sdesc;
	public String test;
	public Sort(int sid, String sname, String sdesc, double sprice) {
		this.sid = sid;
		this.sname = sname;
		this.sprice = sprice;
		this.sdesc = sdesc;
	}
	private Sort(int sid, String sname) {
		this.sid = sid;
		this.sname = sname;
	}
	public Sort() {}
	
	public int getSid() {
		System.out.println("获取sid");
		return sid;
	}
	public void setSid(int sid) {
		this.sid = sid;
	}
	public String getSname() {
		return sname;
	}
	public void setSname(String sname) {
		this.sname = sname;
	}
	public double getSprice() {
		return sprice;
	}
	public void setSprice(Double sprice) {
		this.sprice = sprice;
	}
	public String getSdesc() {
		return sdesc;
	}
	public void setSdesc(String sdesc) {
		//System.out.println(sdesc);
		this.sdesc = sdesc;
	}
	
	@Override
	public String toString() {
		return "Sort [sid=" + sid + ", sname=" + sname + ", sprice=" + sprice + ", sdesc=" + sdesc + "]";
	}	
}
