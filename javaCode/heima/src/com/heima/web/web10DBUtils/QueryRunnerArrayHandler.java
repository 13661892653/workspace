package com.heima.web.web10DBUtils;

import java.sql.Connection;
import java.sql.SQLException;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.ArrayHandler;

import com.heima.data.jdbc.days29.DBUtils.*;
import com.heima.web.web10DBUtils.c3p0.C3P0Utils;

public class QueryRunnerArrayHandler {
	private static Connection conn=C3P0Utils.getConnection();
	public static void main(String[] args) throws SQLException {
		arrayHandler();
	}
	/*
	 * 结果集处理第一种方法， 将结果集第一样存入数组
	 * ArrayHandler
	 */
	public static void arrayHandler() throws SQLException {
		String sql="select * from sort";
		QueryRunner qr=new QueryRunner();
		Object[] result=qr.query(conn, sql, new ArrayHandler());
//		for(int i=0;i<result.length;i++) {
//			System.out.print(result[i]+"\t");
//		}
		for(Object obj:result) {
			System.out.print(obj+"\t");
		}
	}
}
