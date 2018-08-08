package com.heima.web.web10DBUtils.dbcp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import org.junit.Test;

public class TestDBCP {

	@Test
	public void testSelect() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rSet = null;

		try {
			conn = DBCPUtils.getConnection();
			String sql = "select * From user where username= ? ";
			pstmt = conn.prepareStatement(sql);
			pstmt.setObject(1, "colby");
			rSet = pstmt.executeQuery();
			while (rSet.next()) {
				System.out.println(rSet.getString("username"));
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
