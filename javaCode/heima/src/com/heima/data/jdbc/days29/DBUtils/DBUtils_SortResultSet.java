package com.heima.data.jdbc.days29.DBUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.heima.data.jdbc.days29.JDBCUtils;
import com.heima.data.jdbc.days29.Sort;

public class DBUtils_SortResultSet {
	public static void main(String[] args) throws SQLException {
		Connection con=JDBCUtils.getConnection();
		String sql="select sid,sname,sprice,sdesc From sort";
		PreparedStatement pst=con.prepareStatement(sql);
		ResultSet rs=pst.executeQuery();
		
		List<Sort> list=new ArrayList<Sort>();
		while(rs.next()){		
			list.add(
					new Sort(
							rs.getInt("sid")
							,rs.getString("sname")
							,rs.getString("sdesc")
							,rs.getDouble("sprice")
							)
					);
		}
		for(Sort s:list) {
			System.out.println(s.toString());
		}
	}
}
