package com.easyrong.data.thread.days26;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/*
 * 线程池程序
 * 使用Executors中的静态方法创建线程池对象
 * static ExecutorService newFixedThreadPool(int 线程个数) 返回线程池对象
 * 返回的是ExecutorService接口的实现类（线程池对象）
 * 接口实现类对象，调用方submit提交线程执行任务
 */
public class ThreadPoolDemo {
	public static void main(String[] args) {
		//三个线程
		ExecutorService es=Executors.newFixedThreadPool(1);
		es.submit(new SubRunnable());
		es.submit(new SubRunnable());
		es.submit(new SubRunnable());
	}
}
