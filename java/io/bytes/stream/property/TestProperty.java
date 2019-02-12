package io.bytes.stream.property;

import java.util.Properties;
import java.io.*;

/*
 * 解析key＝value文件
 */

public class TestProperty {

	public static void main(String[] args) throws Exception {
		FileInputStream fis = new FileInputStream("./src/io/bytes/stream/property/p.txt");
		Properties p = new Properties();
		p.load(fis);
		String name = p.getProperty("name");
		System.out.println("name: " + name);
		
		String city = p.getProperty("city");
		city = new String(city.getBytes("ISO8859-1"), "UTF-8");	// 编码处理
		System.out.println("city: " + city);
	}
}
