package com.heima.web;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import org.junit.Test;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class TestLogin {
	public void login(String username,String password) throws SQLException {
		Connection conn=JDBCUtilsConfig.getConnection();
		String sql="select * from user where username =? and password = ?";
		PreparedStatement sta=conn.prepareStatement(sql);
		sta.setObject(1, "colby");
		sta.setObject(2, "123456");
		ResultSet rs=sta.executeQuery();
		if(rs.next()){
			System.out.println("恭喜你，登陆成功-"+rs.getObject("username"));
		}else {
			System.out.println("抱歉，用户名或者密码错误！");
		}
		rs.close();
		sta.close();
		conn.close();
	}
	
	@Test
	public void testJunit() throws SQLException {
		login(null, null);
	}
}
