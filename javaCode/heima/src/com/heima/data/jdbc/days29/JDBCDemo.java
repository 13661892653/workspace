package com.heima.data.jdbc.days29;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class JDBCDemo {
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// 注册驱动
		Class.forName("com.mysql.jdbc.Driver");
		String url = "jdbc:mysql://localhost:3306/world?useSSL=false";
		String username = "root";
		String password = "root";
		Connection con = DriverManager.getConnection(url, username, password);
		System.out.println(con);
		Statement stat = con.createStatement();
		String sql = "select * from city";
		ResultSet rs = stat.executeQuery(sql);
		System.out.print(rs);
		while (rs.next()) {
			System.out.println(rs.getInt("id") + "\t" + rs.getString("Name") + "\t" + rs.getString("CountryCode") + "\t"
					+ rs.getString("District") + "\t" + rs.getInt("Population"));
		}
		rs.close();
		stat.close();
		con.close();
	}
}
