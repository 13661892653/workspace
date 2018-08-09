package com.heima.web.web10DBUtils;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.MapListHandler;
import org.junit.Test;

import com.heima.web.web10DBUtils.c3p0.C3P0Utils;

public class QueryUserC3P0Utils {
	private static Connection conn = C3P0Utils.getConnection();

	public static void queryUser() {

		QueryRunner qr = new QueryRunner();
		String sql = "select * from user where id=?";
		Object[] params = { "1" };
		try {
			List<Map<String, Object>> result = qr.query(conn, sql, new MapListHandler(), params);
			for (Map<String, Object> m : result) {
				System.out.println(m);
				for (String key : m.keySet()) {
					System.out.print(key + "=" + m.get(key) + "\t");
				}
				System.out.println("");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Test
	public void testJunit() {
		queryUser();
	}
}
