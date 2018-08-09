package com.heima.web.web10DBUtils;

import java.sql.SQLException;
import java.util.List;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.ArrayListHandler;

import com.heima.data.jdbc.days30.datasource.JDBCUtilsPool;
import com.heima.web.web10DBUtils.dbcp.DBCPUtils;


public class QueryRunnerDemo {
	public static void main(String[] args) throws SQLException {
		insert();
		select();
	}
	
	private static QueryRunner qr=new QueryRunner(DBCPUtils.getDataSource());
	
	public static void insert() throws SQLException {
		String sql="insert into sort(sname,sprice,sdesc) values(?,?,?)";
		Object[] params= {"水果",100,"备注信息"};
		qr.update(sql,params);
	}
	
	public static void select() throws SQLException {
		String sql="select * from sort";
		List<Object[]> result=qr.query(sql, new ArrayListHandler());
		for(Object[] objs:result) {
			for(Object obj:objs) {
				System.out.print(obj+"\t");
			}
			System.out.println();
		}
	}
}
