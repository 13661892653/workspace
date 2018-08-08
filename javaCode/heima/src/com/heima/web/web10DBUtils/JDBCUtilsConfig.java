package com.heima.web.web10DBUtils;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;
/*import java.util.ResourceBundle;*/


public class JDBCUtilsConfig {
	private static Connection conn = null;
	private static String driverClass=null;
	private static String url=null;
	private static String username=null;
	private static String password=null;
	
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
		
		//加载配置文件，不需要加后缀
/*		 * ResourceBundle bundle=ResourceBundle.getBundle("db");
		 * String driver=bundle.getString("driver");*/

		InputStream in = JDBCUtilsConfig.class.getClassLoader().getResourceAsStream("db.properties");
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
	
	public static void release(Connection conn,PreparedStatement ps,ResultSet rs) {
		if(rs!=null)
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		if(ps!=null)
			try {
				ps.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		if(conn!=null)
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
	}
}
