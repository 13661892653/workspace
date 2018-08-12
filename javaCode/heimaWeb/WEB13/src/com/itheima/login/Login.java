package com.itheima.login;

import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;

import javax.servlet.ServletContext;
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

	public void init() {
//		第一次创建servlet对象的时候，初始化域对象变量count
		int count = 0;
		this.getServletContext().setAttribute("count", count);
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		String sql = "select * from user where username=? and password=?";
		System.out.println("conn" + conn);
		User user = null;
		// 记录登录成功的用户数，不考虑同一以用户登录多次
		Integer count = (Integer) this.getServletContext().getAttribute("count");
		this.getServletContext().setAttribute("count", ++count);

		try {
			QueryRunner qr = new QueryRunner();
			user = qr.query(conn, sql, new BeanHandler<User>(User.class), username, password);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			if (user != null) {

				System.out.println(user.toString());
				// 用户登录成功
				response.getWriter().write(user.toString() + "您是第" + count + "位登录成功的用户");
			} else {
				response.getWriter().write("Your user or password is error！");
			}
		}

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
