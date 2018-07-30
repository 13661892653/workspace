package com.heima.data.exception.days21;
/**
 * 	Throwable类中的方法
 * 	三个方法都和异常的信息有关系
 * 	String getMessage() 对异常信息的详细描述
 * 	String toString() 对异常信息的简短描述
 * 	void printStacktrace() 将异常信息追踪到标准的错误流
 * 	@author Administrator
 *
 */
public class ThrowableDemo {
	public static void main(String[] args) {
		try {
			function01();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void function01() throws Exception {
		throw new Exception("系统异常了");
	}
}
