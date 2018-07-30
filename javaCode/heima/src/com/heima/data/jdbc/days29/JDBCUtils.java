package com.heima.data.jdbc.days29;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCUtils {
	private void JDBCUtils() {}
	private static Connection con;
	
	static{
		try {
			Class.forName("com.mysql.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		String url = "jdbc:mysql://localhost:3306/world?useSSL=false";
		String username = "root";
		String password = "root";
		try {
			con = DriverManager.getConnection(url, username, password);
		} catch (SQLException e) {
			System.out.println(e+" 数据库连接失败！");
		}
	}
	
	public static Connection getConnection() {
		return con;
	}
	
	public static void close(Connection con,Statement stat){
		 
		 if(stat!=null){
			 try{
				 stat.close();
			 }catch(SQLException ex){}
		 }
		 
		 if(con!=null){
			 try{
				 con.close();
			 }catch(SQLException ex){}
		 }
		 
	}
	
	public static void close(Connection con,Statement stat , ResultSet rs){
		 if(rs!=null){
			 try{
				 rs.close();
			 }catch(SQLException ex){}
		 }
		 
		 if(stat!=null){
			 try{
				 stat.close();
			 }catch(SQLException ex){}
		 }
		 
		 if(con!=null){
			 try{
				 con.close();
			 }catch(SQLException ex){}
		 }
		 
	}
}
