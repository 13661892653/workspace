package com.heima.web.web09JDBC;

import java.sql.Connection;
import java.sql.PreparedStatement;

import org.junit.Test;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class DeleteDemo {
/**
 * 
 * @param id
 */
	public static void Delete(Integer id) {

		Connection conn = null;
		PreparedStatement sta = null;
		Object rs = null;
		try {
			conn = JDBCUtilsConfig.getConnection();
			String sql = "delete from  user where id=?";
			sta = conn.prepareStatement(sql);
			sta.setObject(1, id);
			rs = sta.executeUpdate();
			System.out.println("删除记录数：" + rs);
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
		Delete(5);
	}
}
