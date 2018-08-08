package com.heima.web.web09JDBC;

import java.sql.Connection;
import java.sql.PreparedStatement;

import org.junit.Test;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class InsertDemo {
/**
 * 
 * @param username
 * @param phone
 * @param password
 */
	public static void Insert(String username, String phone, String password) {

		Connection conn = null;
		PreparedStatement sta = null;
		Object rs = null;
		try {
			conn = JDBCUtilsConfig.getConnection();
			String sql = "insert into user values(null,?,?,?)";
			sta = conn.prepareStatement(sql);
			sta.setObject(1, username);
			sta.setObject(2, phone);
			sta.setObject(3, password);
			rs = sta.executeUpdate();
			System.out.println("插入记录数：" + rs);
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			// 关闭连接，结果集，创建语句对象
			JDBCUtilsConfig.release(conn, sta, null);
		}
	}

	@Test
	public void testJunit() {
		// 测试Select方法
		Insert("colby", "13688888888", "123456");
	}
}
