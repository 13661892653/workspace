package com.heima.web.web08;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import org.junit.Test;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class TestLogin {
	public void login(String username, String password) throws SQLException {
		// 获取连接
		Connection conn = JDBCUtilsConfig.getConnection();
		// 书写SQL语句
		String sql = "select * from user where username =? and password = ?";
		// 创建预处理对象：PrepareStatement，建议不用createStatement
		PreparedStatement ps = conn.prepareStatement(sql);
		// 设置参数(给占位符，1代表第一个问号，2代表第二个问号)
		ps.setObject(1, username);
		ps.setObject(2, password);
		// 打印sql编译后的语句，输出到屏幕
		System.out.println(ps);
		// 执行查询操作
		ResultSet rs = ps.executeQuery();
		if (rs.next()) {
			System.out.println("恭喜你，登陆成功-" + rs.getObject("username"));
		} else {
			System.out.println("抱歉，用户名或者密码错误！");
		}
		// 关闭对象与数据库链接
		JDBCUtilsConfig.release(conn,ps,rs);
	}

	@Test
	public void testJunit() throws SQLException {
		login("chen", "123456");
	}
}
