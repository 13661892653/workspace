package com.heima.data.jdbc.days30.datasource;


import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;

import org.apache.commons.dbcp.BasicDataSource;

public class JDBCUtilsPool {

	private static BasicDataSource dataSource=new BasicDataSource();
	
	static {
		dataSource.setDriverClassName("com.mysql.jdbc.Driver");
		dataSource.setUrl("jdbc:mysql://localhost:3306/world?useSSL=false");
		dataSource.setUsername("root");
		dataSource.setPassword("root");
		
		//以下可选，不设置也有默认的
		dataSource.setInitialSize(10);//初始化的链接数
		dataSource.setMaxActive(8);//最大连接数
		dataSource.setMaxIdle(5);//最大空闲数
		dataSource.setMinIdle(1);//最小空闲数
	}
	
	public static DataSource getDataSource() {
		return dataSource;
	}
	
	public static Connection getConnection() {
		try {
			return dataSource.getConnection();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			throw new RuntimeException();
		}
	}
}
