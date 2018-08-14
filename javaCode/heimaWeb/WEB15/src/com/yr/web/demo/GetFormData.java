package com.yr.web.demo;

import java.io.IOException;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class GetFormData
 */
public class GetFormData extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public GetFormData() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// 单值获取
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		System.out.println("======================================");
		// 获取多个值
		String[] like = request.getParameterValues("like");
		System.out.println("username:" + username + " password:" + password);
		// 获取复选框多个值
		if (like != null) {
			for (int i = 0; i < like.length; i++) {
				System.out.println(like[i]);
			}
		}

		System.out.println("======================================");
		Map<String, String[]> parameterMap = request.getParameterMap();
		// 遍历Map的第一种方法keySet
		for (String key : parameterMap.keySet()) {
			for (int i = 0; i < parameterMap.get(key).length; i++) {
				System.out.println(key + ":" + parameterMap.get(key)[i]);
			}
		}

		System.out.println("======================================");
		// 遍历Map的第二种方法entrySet
		for (Map.Entry<String, String[]> entry : parameterMap.entrySet()) {
			System.out.println("key:" + entry.getKey());
			for (String value : entry.getValue()) {
				System.out.println("value:" + value);
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
