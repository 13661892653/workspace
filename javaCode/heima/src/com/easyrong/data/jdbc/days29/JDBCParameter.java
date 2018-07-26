package com.easyrong.data.jdbc.days29;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JDBCParameter {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Class.forName("com.mysql.jdbc.Driver");
		String url = "jdbc:mysql://localhost:3306/world?useSSL=false";
		String username = "root";
		String password = "root";
		Connection con = DriverManager.getConnection(url, username, password);
		String sql="select * From city where CountryCode=? and District=?";
		PreparedStatement pst=con.prepareStatement(sql);
		//传入？对应的参数
		pst.setObject(1, "CHN");
		pst.setObject(2, "Sichuan");
		//ResultSet rs=pst.executeQuery()如果没有预编译，executeQuery需要加入参数sql
		ResultSet rs=pst.executeQuery();
		System.out.println(sql);
		while (rs.next()) {
			System.out.println(rs.getInt("id") + "\t" + rs.getString("Name") + "\t" + rs.getString("CountryCode") + "\t"
					+ rs.getString("District") + "\t" + rs.getInt("Population"));
		}
		rs.close();
		pst.close();
		con.close();
	}

}
