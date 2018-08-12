package com.yr.demo;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ServletDemo
 */
public class ServletDemo extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public ServletDemo() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		//设置状态码
		//response.setStatus(404);
		//增加日期头
		//response.addDateHeader("define", 300000);
		//增加日期头
		//response.addHeader("user", "自定义的字符创");
		//response.setStatus(302);
		//response.setHeader("Location", "http://www.baidu.com");
		//设定定时刷新
		//response.setHeader("refresh", "5;http://www.baidu.com");
		//告诉客户端用utf-8解码，设定客户端的字符编码格式
		//response.setHeader("Content-Type", "text/html;charset=utf-8");
		//设置response查询的码表，可以省略掉，tomcat根据Content-Type的内容设定缓冲区字符编码
		//response.setCharacterEncoding("utf-8");
		//更简单的设置Content-Type的方法
//		response.setContentType("text/html;charset=utf-8");
//		response.getWriter().write("中文显示");
		ServletOutputStream outputStream=response.getOutputStream();
		String realPath=this.getServletContext().getRealPath("pdd.jpg");
		InputStream in=new FileInputStream(realPath);
		
		int len=0;
		byte[] bytes=new byte[1024];
		while((len=in.read(bytes))>0) {
			outputStream.write(bytes,0,len);
		}
		in.close();
		outputStream.close();
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
