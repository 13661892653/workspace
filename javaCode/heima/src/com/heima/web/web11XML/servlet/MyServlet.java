package com.heima.web.web11XML.servlet;

import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.junit.Test;

import com.heima.data.set.days20.Person;

public class MyServlet {

	@Test
	public void testJunit() {
		try {
			// 创建解析器对象
			SAXReader saxReader = new SAXReader();
			// 通过解析器加载xml文件
			Document document = saxReader.read("src/com/heima/web/web11XML/servlet/web.xml");
			// 获取root节点
			Element rootElement = document.getRootElement();
			// 根据元素名称获取子元素节点
			Element servletElement = rootElement.element("servlet");
			String className = servletElement.element("servlet-class").getText();
			try {
				// 加载Person类
				Class clazz = Class.forName(className);
				// 创建实例对象
				Person p = (Person) clazz.newInstance();
				// 设置值
				p.setAge(30);
				p.setName("colby");
				// 打印Person对象
				System.out.println(p.toString());
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		} catch (DocumentException e) {
			e.printStackTrace();
		}
	}
}
