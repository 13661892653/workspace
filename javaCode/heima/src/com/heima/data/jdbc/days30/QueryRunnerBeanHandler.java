package com.heima.data.jdbc.days30;

import java.sql.Connection;
import java.sql.SQLException;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;

import com.heima.data.jdbc.days29.Sort;
import com.heima.data.jdbc.days29.DBUtils.*;

public class QueryRunnerBeanHandler {
	private static Connection conn=JDBCUtilsConfig.getConnection();
	public static void main(String[] args) throws SQLException {
		beanHandler();
	}
	/*
	 * 结果集处理第3种方法，奖结果集第一行存储到JavaBean对象中
	 * BeanHandler
	 * 注意：
	 * 
	 */
	public static void beanHandler() throws SQLException {
		
		String sql="select * from sort";
		QueryRunner qr=new QueryRunner();
		//传入的是Sort类的class文件
		Sort result = qr.query(conn, sql,new BeanHandler<Sort>(Sort.class));
//		for(int i=0;i<result.length;i++) {
//			System.out.print(result[i]+"\t");
//		}
				System.out.print(result+"\t");

	}
}