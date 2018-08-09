package com.heima.web.web10DBUtils;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.MapListHandler;

import com.heima.web.web10DBUtils.c3p0.C3P0Utils;

public class QueryRunnerMapListHandler {
	private static Connection conn=C3P0Utils.getConnection();
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
		
		String sql="select * from sort where sid=?";
		QueryRunner qr=new QueryRunner();
		//定义一个Object数组，传入查询条件
		Object[] params= {"1"};
		//传入的是Sort类的class文件
		List<Map<String, Object>> result = qr.query(conn, sql,new MapListHandler(),params);
		for(Map<String, Object> m:result) {
			for(String key:m.keySet()) {
				System.out.print(key+"="+m.get(key)+"\t");
			}
			System.out.println("");
		}
	}
}