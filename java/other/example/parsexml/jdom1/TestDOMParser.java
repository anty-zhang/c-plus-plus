package xml.jdom1;

import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

//Jdom解析xml文件的第二中方式：用sun提供的API
public class TestDOMParser {
	public static void main(String[] args) {
		TestDOMParser tp = new TestDOMParser();
		tp.parseXMLFile("./day26/xml/jdom/student.xml");
	}

	public void parseXMLFile(String fileName) {
		try {
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			DocumentBuilder db = dbf.newDocumentBuilder();

			// 解析文件名传入
			Document doc = db.parse(fileName);
			// 获得Documet,与xml建立对象匹配
			// Document doc = parser.getDocument();

			// 获得根节点StudentInfo
			Element elmtInfo = doc.getDocumentElement();

			// 得到所有student节点,节点集合
			NodeList nlStudent = elmtInfo.getElementsByTagName("student");

			System.out.println("XML文件开始解析");

			// 循环输出每一个学生成绩

			for (int i = 0; i < nlStudent.getLength(); i++) {

				// 当前student元素
				Element elmtStudent = (Element) nlStudent.item(i);
				// Name/sex/lesson节点清单
				NodeList nlCurrent = elmtStudent.getElementsByTagName("name");
				System.out.println("姓名:"
						+ nlCurrent.item(0).getFirstChild().getNodeValue());

				nlCurrent = elmtStudent.getElementsByTagName("sex");
				System.out.println("性别:"
						+ nlCurrent.item(0).getFirstChild().getNodeValue());
				// 取得Lesson节点,不是一个,需要循环
				nlCurrent = elmtStudent.getElementsByTagName("lesson");

				for (int j = 0; j < nlCurrent.getLength(); j++) {
					// Lesson这个元素的对应
					Element elmtLesson = (Element) nlCurrent.item(j);
					NodeList nlLesson = elmtLesson
							.getElementsByTagName("lessonName");
					System.out.print(nlLesson.item(0).getFirstChild()
							.getNodeValue());
					System.out.print(":");
					nlLesson = elmtLesson.getElementsByTagName("lessonScore");
					System.out.print(nlLesson.item(0).getFirstChild()
							.getNodeValue());
					System.out.println();
				}

				System.out.println("------------------------------------");
			}

			System.out.println("XML文件解析结束");
		} catch (IOException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
