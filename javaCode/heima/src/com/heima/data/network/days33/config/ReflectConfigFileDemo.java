package com.heima.data.network.days33.config;

import java.io.FileReader;
import java.lang.reflect.Method;
import java.util.Properties;

public class ReflectConfigFileDemo {
	public static void main(String[] args) throws Exception {
		// 工程根目录的配置文件不需要再加路径
		FileReader fr = new FileReader("config.properties");
		Properties p = new Properties();
		p.load(fr);
		fr.close();

		String className = p.getProperty("className");
		String methodName = p.getProperty("methodName");

		Class c = Class.forName(className);
		Object obj = c.newInstance();
		Method method = c.getMethod(methodName);
		method.invoke(obj);
	}
}
