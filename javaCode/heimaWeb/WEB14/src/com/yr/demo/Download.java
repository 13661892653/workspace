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
 * Servlet implementation class Download
 */
public class Download extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Download() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// 获得要下载的问价的名称
		String filename = request.getParameter("filename");
		String realPath = request.getServletContext().getRealPath("download/" + filename);
		// 要下载的这个文件的类型，客户端通过文件的MIME类型区分类型
		response.setContentType(this.getServletContext().getMimeType(realPath));
		// 告诉客户端该文件不是直接解析而是以附件的形式打开，就是下载
		response.setHeader("Content-Disposition", "attachment;filename=" + filename);
		// 通过response获取输出流，用于向客户端写内容
		ServletOutputStream outputStream = response.getOutputStream();
		// new输入流，用于读入下载文件的字节流
		InputStream in = new FileInputStream(realPath);
		System.out.println("filename：" + filename);
		// 文件写入的固定写法
		int len = 0;
		byte[] bytes = new byte[1024];
		while ((len = in.read(bytes)) > 0) {
			outputStream.write(bytes, 0, len);
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
