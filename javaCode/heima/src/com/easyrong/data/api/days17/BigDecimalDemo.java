package com.easyrong.data.api.days17;

import java.math.BigDecimal;

public class BigDecimalDemo {
	public static void main(String[] args) {
		BigDecimal bigDecimal01=new BigDecimal("100000000000000000000000000001");
		BigDecimal bigDecimal02=new BigDecimal("100000000000000000000000000009");
		BigDecimal add=bigDecimal01.add(bigDecimal02);
		BigDecimal multiply=bigDecimal01.multiply(bigDecimal02);
		System.out.println(add);
		System.out.println(multiply);
		
		System.out.println(0.09+0.01);
	}
}
