package com.heima.data.jdbc.days30.DBUtils;

import java.sql.Connection;
import java.sql.SQLException;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.ArrayHandler;

import com.heima.data.jdbc.days29.DBUtils.JDBCUtilsConfig;

public class ResultArrayHandler {

	private static Connection conn = JDBCUtilsConfig.getConnection();

	public static void main(String[] args) throws SQLException {
		arrayHandler();
	}

	public static void arrayHandler() throws SQLException {
		QueryRunner qr = new QueryRunner();
		String sql = "select * From sort";
		qr.query(conn, sql, new ArrayHandler());
		Object[] result = qr.query(conn, sql, new ArrayHandler());
//		for(int i=0;i<result.length;i++) {
//			System.out.print(result[i]+"\t");
//		}
		for (Object obj : result) {
			System.out.print(obj + "\t");
		}
	}
}
