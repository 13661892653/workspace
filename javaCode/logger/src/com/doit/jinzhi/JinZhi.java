package com.doit.jinzhi;

public class JinZhi {

	public static void main(String[] args) {

		byte[] b1 = new byte[] { 0x00 };
		for (byte b : b1) {
			System.out.println(b);
		}

		byte[] b2 = new byte[] { 0 };
		for (byte b : b2) {
			System.out.println(b);
		}

		byte[] b3 = "0".getBytes();
		for (byte b : b3) {
			System.out.println(b);

		}

		byte[] b4 = new byte[] { 8 };
		for (byte b : b4) {
			System.out.println(b);
		}

		byte[] b5 = new byte[] { 07 };
		for (byte b : b5) {
			System.out.println(b);
		}

		byte[] b6 = "\000".getBytes();
		for (byte b : b6) {
			System.out.println(b);
		}

		byte[] b7 = "000".getBytes();
		for (byte b : b7) {
			System.out.println(b);
		}

		byte[] b8 = "000".getBytes();
		for (byte b : b7) {
			System.out.println(b);
		}

		String c = "0" + "\000";
		byte[] b9 = c.getBytes();
		for (byte b : b9) {
			System.out.println(b);
		}
		String d = "0" + "0";
		byte[] b10 = d.getBytes();
		for (byte b : b10) {
			System.out.println(b);
		}

	}

}
