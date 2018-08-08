package com.heima.web.web09;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import org.junit.Test;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class SelectDemo {

	public static void Select(String username) {

		Connection conn = null;
		PreparedStatement sta = null;
		ResultSet rs = null;
		try {
			conn = JDBCUtilsConfig.getConnection();
			String sql = "select * From user where username=?";
			sta = conn.prepareStatement(sql);
			sta.setObject(1, username);
			rs = sta.executeQuery();
			while (rs.next()) {
				// System.out.println("");
				System.out.println(rs.getObject("id") + "--" + rs.getObject("username") + "--" + rs.getObject("phone"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			// 关闭连接，结果集，创建语句对象
			JDBCUtilsConfig.release(conn, sta, rs);
		}

	}

	@Test
	public void testJunit() {
		//测试Select方法
		Select("colby");
	}
}
