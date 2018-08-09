package com.heima.web.web11XML.dom4j;

import java.util.List;

import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.junit.Test;

public class TestDom4j {

	@Test
	public void testJunit() {
		try {
			// 获得解析器
			SAXReader saxReader = new SAXReader();
			// 获取document文档对象
			Document document = saxReader.read("src/com/heima/web/web11XML/xml/schemaDemo.xml");
			// 获取根元素
			Element rootElement = document.getRootElement();
			// 获取根元素的标签名称
			System.out.println(rootElement.getName());
			// 获取根元素的属性
			System.out.println(rootElement.attributeValue("version"));

			List<Element> elements = rootElement.elements();
			for (Element element : elements) {
				System.out.println(element.getName());
				// 判断当前元素是否为servlet
				if ("servlet".equals(element.getName())) {
					// 获取servlet下的servlet-name、servlet-class元素
					Element element2 = element.element("servlet-name");
					Element element3 = element.element("servlet-class");
					System.out.println(element2.getText() + "\t" + element3.getText());
				}
			}
		} catch (DocumentException e) {
			e.printStackTrace();
		}
	}
}
