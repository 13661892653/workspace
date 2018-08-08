package com.heima.web.web10DBUtils.c3p0;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import org.junit.Test;

import com.heima.web.web10DBUtils.JDBCUtilsConfig;

public class TestC3P0 {

	@Test
	public void testJunit() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		// 默认加载<default-config>配置文件
		// ComboPooledDataSource dataSource=new ComboPooledDataSource();
		// ComboPooledDataSource指定名称的话，则调用<named-config name="yr">的配置文件
		// ComboPooledDataSource dataSource=new ComboPooledDataSource("yr");
		try {
			conn = C3P0Utils.getConnection();
			String sql = "select * from user where username='colby'";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				System.out.println(rs.getString("id") + "\t" + rs.getString("phone") + "\t" + rs.getString("username"));
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			JDBCUtilsConfig.release(conn, pstmt, rs);
		}
	}
}
