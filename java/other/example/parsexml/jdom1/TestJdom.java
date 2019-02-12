package xml.jdom1;

import java.io.FileOutputStream;
import java.util.List;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.input.SAXBuilder;
import org.jdom.output.XMLOutputter;
//Jdom解析xml文件地一种实现方式：用jdom.jar
public class TestJdom {
	public static void main(String[] args) {
		try {
			//1.用SAXBuilder将xml文件加载到内存
			SAXBuilder sax = new SAXBuilder();
			//2.用Document获得加载到内存中的xml文件的对象
			Document doc = sax.build("./src/xml/jdom1/student.xml");
			//3.获得父节点
			Element el = doc.getRootElement();
			//4.获得父节点
			List<Element> childList = el.getChildren("student");
			for(Element student:childList){
				//5.用getChildTextTrim("")获得标记的名称
				System.out.println("Student name--->"+student.getChildTextTrim("name"));
				System.out.println("Student sex--->"+student.getChildTextTrim("sex"));
				
				//打印属性值
				System.out.println("student id ---- >"+student.getAttributeValue("id"));
				
				//修改属性值
				student.setAttribute("id", "10");
				
				
				//取节点，并修改内容
				Element ele = student.getChild("name");
				ele.setText("zhangqiang");
				
				List<Element> studentChildList = student.getChildren("lesson");
				
				for(Element lession:studentChildList){
					System.out.println("lessonName--->"+lession.getChildTextTrim("lessonName"));
					System.out.println("lessonScore--->"+lession.getChildTextTrim("lessonScore"));
				}
				System.out.println();
			}
			
			//输出修改后的结果
			XMLOutputter out = new XMLOutputter();
			out.output(doc, new FileOutputStream("./src/xml/jdom1/student.xml"));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
