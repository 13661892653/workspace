package com.itheima.login;

import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;

import com.itheima.utils.C3P0Utils;
import com.itheima.domain.User;

/**
 * Servlet implementation class QuickStartServlet
 */
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private static Connection conn = C3P0Utils.getConnection();

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Login() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		String sql = "select * from user where username=? and password=?";
		System.out.println("conn" + conn);
		User user = null;
		try {
			QueryRunner qr = new QueryRunner();
			user = qr.query(conn, sql, new BeanHandler<User>(User.class), username, password);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			if (user != null) {
				// 用户登录成功
				response.getWriter().write(user.toString());
			} else {
				response.getWriter().write("Your user or password is error！");
			}
		}

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
