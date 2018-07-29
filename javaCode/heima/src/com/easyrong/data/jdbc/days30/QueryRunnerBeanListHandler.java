package com.easyrong.data.jdbc.days30;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;

import com.easyrong.data.jdbc.days29.Sort;
import com.easyrong.data.jdbc.days29.DBUtils.*;

public class QueryRunnerBeanListHandler {
	private static Connection conn=JDBCUtilsConfig.getConnection();
	public static void main(String[] args) throws SQLException {
		beanListHandler();
	}
	/*
	 * 结果集处理第4种方法，奖结果集第一行存储到JavaBeanList对象中
	 * BeanListHandler
	 * 注意：
	 * 
	 */
	public static void beanListHandler() throws SQLException {
		
		String sql="select * from sort";
		QueryRunner qr=new QueryRunner();
		//传入的是Sort类的class文件
		List<Sort> result = qr.query(conn, sql,new BeanListHandler<Sort>(Sort.class));
		for(Sort s:result) {
			
			System.out.println(s);
		}

	}
}