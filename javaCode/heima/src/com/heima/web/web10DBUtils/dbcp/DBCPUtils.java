package com.heima.web.web10DBUtils.dbcp;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;
/*import java.util.ResourceBundle;*/

import javax.sql.DataSource;

import org.apache.commons.dbcp.BasicDataSourceFactory;

public class DBCPUtils {
	private static DataSource dataSource;

	static {
		try {
			InputStream in = DBCPUtils.class.getClassLoader().getResourceAsStream("db.properties");
			Properties pro = new Properties();
			// 将输入流加载到Properties集合中
			pro.load(in);
			dataSource = BasicDataSourceFactory.createDataSource(pro);
		} catch (Exception e) {
			throw new RuntimeException("配置文件加载异常！");
		}
	}

	public static DataSource getDataSource() {
		return dataSource;
	}
	
	public static Connection getConnection() {
		try {
			return dataSource.getConnection();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
}
