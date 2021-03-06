package com.yr.demo;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import sun.misc.BASE64Encoder;

/**
 * Servlet implementation class Download
 */
public class DownloadCN extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public DownloadCN() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		/*
		 * 文件是中文名称的文件下载 获取中文参数，filename
		 */
		// 获得要下载的问价的名称
		String filename = request.getParameter("filename");
		// 解决获得中文参数的乱码----下节课讲
		filename = new String(filename.getBytes("ISO8859-1"), "UTF-8");// 人物.jpg

		// 获得请求头中的User-Agent
		String agent = request.getHeader("User-Agent");
		// 根据不同浏览器进行不同的编码
		String filenameEncoder = "";
		if (agent.contains("MSIE")) {
			// IE浏览器
			filenameEncoder = URLEncoder.encode(filename, "utf-8");
			filenameEncoder = filenameEncoder.replace("+", " ");
		} else if (agent.contains("Firefox")) {
			// 火狐浏览器
			BASE64Encoder base64Encoder = new BASE64Encoder();
			filenameEncoder = "=?utf-8?B?" + base64Encoder.encode(filename.getBytes("utf-8")) + "?=";
		} else {
			// 其它浏览器
			filenameEncoder = URLEncoder.encode(filename, "utf-8");
		}

		// 要下载的这个文件的类型，客户端通过文件的MIME类型区分类型
		response.setContentType(this.getServletContext().getMimeType(filename));
		// 告诉客户端该文件不是直接解析而是以附件的形式打开，就是下载，客户端默认对名字进行解码
		response.setHeader("Content-Disposition", "attachment;filename=" + filenameEncoder);
		System.out.println("filename:" + filename);
		// 通过response获取输出流，用于向客户端写内容
		ServletOutputStream outputStream = response.getOutputStream();
		// new输入流，用于读入下载文件的字节流
		// 获取文件的绝对路径
		String realPath = request.getServletContext().getRealPath("download/" + filename);
		InputStream in = new FileInputStream(realPath);
		System.out.println("filename：" + filenameEncoder);
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
