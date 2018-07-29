package com.easyrong.data.jdbc.days30;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.MapListHandler;

import com.easyrong.data.jdbc.days29.DBUtils.*;

public class QueryRunnerMapListHandler {
	private static Connection conn=JDBCUtilsConfig.getConnection();
	public static void main(String[] args) throws SQLException {
		mapListHandler();
	}
	/*
	 * 结果集处理第8种方法，奖结果集第一行存储到JavaBeanList对象中
	 * MapListHandler
	 * 注意：
	 * 
	 */
	public static void mapListHandler() throws SQLException {
		
		String sql="select * from sort";
		QueryRunner qr=new QueryRunner();
		//传入的是Sort类的class文件
		List<Map<String, Object>> result = qr.query(conn, sql,new MapListHandler());
		for(Map<String, Object> m:result) {
			for(String key:m.keySet()) {
				System.out.print(key+"="+m.get(key)+"\t");
			}
			System.out.println("");
		}
	}
}