package xml.sax;

import org.xml.sax.SAXException;
import org.xml.sax.XMLReader;
import org.xml.sax.helpers.XMLReaderFactory;

public class TestSAX {
	public static void main(String[] args) {
		TestSAX sax = new TestSAX();
		sax.parse("./src/xml/sax/student.xml");
	}
	
	/**
	 * 解析文档
	 * 
	 * @param fileName
	 *            XML文件的名字
	 */
	public void parse(String filePath){
		try {
			//通过阅读解析起的工厂，创建一个阅读解析器
			XMLReader parser = XMLReaderFactory.createXMLReader();
			//处理内容前注册内容管理器
			parser.setContentHandler(new XMLContentHandler());
			//开始解析
			parser.parse(filePath);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
