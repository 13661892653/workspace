package com.easyrong.data.io.days25;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;
import java.util.Set;

public class PropertiesDemo {
	public static void main(String[] args)  throws IOException{
		properties();
		readPropertiesFile();
	}
	
	public static void properties() {
		Properties pro=new Properties();
		pro.setProperty("name", "colby");
		pro.setProperty("age", "20");
		pro.setProperty("set", "man");
		System.out.println(pro);
		System.out.println(pro.getProperty("age"));
		Set<String> set=pro.stringPropertyNames();//跟keySet类似，entrySet
		for(String key:set) {
			System.out.println(key+"->"+pro.getProperty(key));
		}
	}
	
	public static void readPropertiesFile() throws IOException {
		Properties pro=new Properties();
		FileReader fr=
				new FileReader("E:\\project\\workspace\\javaCode\\heima\\src\\com\\easyrong\\data\\io\\days25\\application.properties");
		pro.load(fr);
		Set<String> set=pro.stringPropertyNames();
		for(String key:set) {
			System.out.println(key+"="+pro.getProperty(key));
		}
	}
}
