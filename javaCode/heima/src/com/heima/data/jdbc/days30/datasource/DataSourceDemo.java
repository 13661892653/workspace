package com.heima.data.jdbc.days30.datasource;

import java.sql.Connection;
import java.sql.SQLException;

import org.apache.commons.dbcp.BasicDataSource;

public class DataSourceDemo {
	public static void main(String[] args) throws SQLException {
		BasicDataSource dataSource=new BasicDataSource();
		dataSource.setDriverClassName("com.mysql.jdbc.Driver");
		dataSource.setUrl("jdbc:mysql://localhost:3306/world");
		dataSource.setUsername("root");
		dataSource.setPassword("root");
		Connection con=dataSource.getConnection();
		System.out.println(con);
	}
}
