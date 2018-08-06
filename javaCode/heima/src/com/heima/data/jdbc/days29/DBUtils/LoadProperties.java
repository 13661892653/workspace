package com.heima.data.jdbc.days29.DBUtils;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class LoadProperties {
	/*
	 * 加载properties文件到集合中
	 */
	public static void main(String[] args) throws IOException, ClassNotFoundException, SQLException {
		//加载配置文件到输入流
		InputStream in=LoadProperties.class.getClassLoader().getResourceAsStream("db.properties");
		Properties pro=new Properties();
		//将输入流加载到Properties集合中
		System.out.println("xxxxxxxxxxxx");
		pro.load(in);
		System.out.println(pro);
		//从集合中根据键值获取Value
		String driverClass=pro.getProperty("driverClass");
		String url=pro.getProperty("url");
		String username=pro.getProperty("username");
		String password=pro.getProperty("password");
		//测试连接是佛正常，打印链接信息
		Class.forName(driverClass);
		Connection conn=DriverManager.getConnection(url, username, password);
		System.out.println(conn);
	}
}
