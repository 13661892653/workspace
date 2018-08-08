package com.heima.web.web10DBUtils;

import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLFeatureNotSupportedException;
import java.util.LinkedList;
import java.util.logging.Logger;

import javax.sql.DataSource;

import org.junit.Test;

public class MyDataSource implements DataSource {
	// 创建1个容器用于存储Connection对象
	private static LinkedList<Connection> pool = new LinkedList<Connection>();
	// 创建五个连接，放到LinkedList容器中去
	static {
		for (int i = 0; i < 5; i++) {
			Connection conn = JDBCUtilsConfig.getConnection();
			pool.add(conn);
		}
	}

	@Override
	public Connection getConnection() throws SQLException {
		Connection conn = null;
		if (pool.size() == 0) {
			for (int i = 0; i < 5; i++) {
				conn = JDBCUtilsConfig.getConnection();
				pool.add(conn);
			}
		}
		// 从pool获取一个链接返回
		return pool.remove(0);
	}

	public void backConnection(Connection conn) {
		// 将连接放回连接池，不要close
		pool.add(conn);
	}

	@Override
	public PrintWriter getLogWriter() throws SQLException {
		return null;
	}

	@Override
	public void setLogWriter(PrintWriter out) throws SQLException {
	}

	@Override
	public void setLoginTimeout(int seconds) throws SQLException {
	}

	@Override
	public int getLoginTimeout() throws SQLException {
		return 0;
	}

	@Override
	public Logger getParentLogger() throws SQLFeatureNotSupportedException {
		return null;
	}

	@Override
	public <T> T unwrap(Class<T> iface) throws SQLException {
		return null;
	}

	@Override
	public boolean isWrapperFor(Class<?> iface) throws SQLException {
		return false;
	}

	@Override
	public Connection getConnection(String username, String password) throws SQLException {
		return null;
	}

	@Test
	public void testJunit() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		MyDataSource myDataSource = new MyDataSource();
		try {
			conn = myDataSource.getConnection();
			String sql = "select * from user where username='colby'";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			System.out.println(rs);
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			myDataSource.backConnection(conn);
		}
	}

}
