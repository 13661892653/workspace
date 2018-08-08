package com.heima.web.web10DBUtils;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.ArrayListHandler;

import com.heima.data.jdbc.days29.DBUtils.*;

public class QueryRunnerArrayListHandler {
	private static Connection conn=JDBCUtilsConfig.getConnection();
	public static void main(String[] args) throws SQLException {
		arrayListHandler();
	}
	/*
	 * 结果集处理第2种方法，奖结果集全部存入List集合中
	 * ArrayListHandler
	 */
	public static void arrayListHandler() throws SQLException {
		
		String sql="select * from sort";
		QueryRunner qr=new QueryRunner();
		List<Object[]> result=qr.query(conn, sql, new ArrayListHandler());
//		for(int i=0;i<result.length;i++) {
//			System.out.print(result[i]+"\t");
//		}
		for(Object[] obj:result) {
			for(int i=0;i<obj.length;i++) {
				System.out.print(obj[i]+"\t");
			}
			System.out.print("\n");
		}
	}
}