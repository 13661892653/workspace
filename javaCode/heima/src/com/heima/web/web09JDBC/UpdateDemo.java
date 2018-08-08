package com.heima.web.web09JDBC;

import java.sql.Connection;
import java.sql.PreparedStatement;

import org.junit.Test;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class UpdateDemo {
	/**
	 * 
	 * @param username
	 * @param phone
	 * @param password
	 * @param id
	 */

	public static void Update(String username, String phone, String password, Integer id) {

		Connection conn = null;
		PreparedStatement sta = null;
		Object rs = null;
		try {
			conn = JDBCUtilsConfig.getConnection();
			String sql = "update user set username=?,phone=?,password=? where id=?";
			sta = conn.prepareStatement(sql);
			sta.setObject(1, username);
			sta.setObject(2, phone);
			sta.setObject(3, password);
			sta.setObject(4, id);
			rs = sta.executeUpdate();
			System.out.println("更新记录数：" + rs);
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
		Update("lisi", "13688888888", "123456", 4);
	}
}
