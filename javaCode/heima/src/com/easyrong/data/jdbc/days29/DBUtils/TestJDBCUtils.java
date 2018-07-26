package com.easyrong.data.jdbc.days29.DBUtils;

import java.sql.Connection;

public class TestJDBCUtils {
	public static void main(String[] args) {
		Connection conn=JDBCUtilsConfig.getConnection();
		System.out.println(conn);
	}
}
