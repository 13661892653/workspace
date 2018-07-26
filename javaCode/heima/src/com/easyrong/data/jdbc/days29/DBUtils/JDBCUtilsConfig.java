package com.easyrong.data.jdbc.days29.DBUtils;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;


public class JDBCUtilsConfig {
	private static Connection conn = null;
	private static String driverClass;
	private static String url;
	private static String username;
	private static String password;

	static {
		readConfig();
		// 测试连接是佛正常，打印链接信息
		try {
			Class.forName(driverClass);
		} catch (ClassNotFoundException e) {
			throw new RuntimeException("数据驱动类加载异常！");
		}
		try {
			conn = DriverManager.getConnection(url, username, password);
		} catch (SQLException e) {
			throw new RuntimeException("数据连接异常！");
		}
	}

	private static void readConfig() {
		InputStream in = LoadProperties.class.getClassLoader().getResourceAsStream("db.properties");
		Properties pro = new Properties();
		// 将输入流加载到Properties集合中
		try {
			pro.load(in);
		} catch (IOException e) {
			throw new RuntimeException("配置文件加载异常！");
		}
		// 从集合中根据键值获取Value
		driverClass = pro.getProperty("driverClass");
		url = pro.getProperty("url");
		username = pro.getProperty("username");
		password = pro.getProperty("password");
	}

	public static Connection getConnection() {
		return conn;
	}
}
