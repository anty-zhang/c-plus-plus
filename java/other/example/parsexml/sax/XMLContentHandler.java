package xml.sax;

import org.xml.sax.Attributes;
import org.xml.sax.ContentHandler;
import org.xml.sax.Locator;
import org.xml.sax.SAXException;

public class XMLContentHandler implements ContentHandler {

	// DTD中定义的元素名
	private static final String ELEMENT_NAME = "name";

	private static final String ELEMENT_SEX = "sex";

	private static final String ELEMENT_LESSON = "lesson";

	private static final String ELEMENT_LESSON_NAME = "lessonName";

	private static final String ELEMENT_LESSON_SCORE = "lessonScore";

	private static final String ELEMENT_STUDENT = "student";

	private static final String ELEMENT_LINE = "breakLine";

	// 当前元素的数据
	private String currentData = "";

	private String lessonName = "";

	private String lessonScore = "";

	/**
	 * 取得元素数据
	 * 
	 * @param ch
	 * @param start
	 * @param length
	 */
	public void characters(char[] ch, int start, int length)
			throws SAXException {
		System.out.println("已经取得数据");
		currentData = new String(ch,start,length).trim(); 
	}

	/**
	 * 在解析整个文档结束时调用
	 */

	public void endDocument() throws SAXException {
		System.out.println("－－－－－解析XML文件结束－－－－－");
	}

	/**
	 * 在解析元素结束时调用
	 * 
	 * @param namespaceURI
	 * @param localName
	 *            本地名，如student
	 * @param qName
	 *            原始名
	 */
	public void endElement(String uri, String localName, String qName)
			throws SAXException {
		if (localName.equals(ELEMENT_NAME)) {
			System.out.println(localName+"-->"+currentData);
		}else if(localName.equals(ELEMENT_SEX)){
			System.out.println(localName+"-->"+currentData);
		}else if(localName.equals(ELEMENT_LESSON_NAME)){
			this.lessonName = currentData;
		}else if(localName.equals(ELEMENT_LESSON_SCORE)){
			this.lessonScore = currentData;
		}else if(localName.equals(ELEMENT_LESSON)){
			System.out.println(lessonName+"<-->"+lessonScore);
		}else if(localName.equals(ELEMENT_LINE)){
			System.out.println("---------------------");
		}
	}

	/**
	 * 在解析命名空间结束时调用
	 */
	public void endPrefixMapping(String prefix) throws SAXException {
		// TODO Auto-generated method stub

	}

	/**
	 * 取得元素数据中的空白
	 * 
	 * @param ch
	 * @param start
	 * @param length
	 */
	public void ignorableWhitespace(char[] ch, int start, int length)
			throws SAXException {
		// TODO Auto-generated method stub

	}

	/**
	 * 在解析到处理指令时，调用此方法。 这些处理指令不包括XML的版权指令，它由解析器本身识别。
	 * 
	 * @param target
	 * @param data
	 */
	public void processingInstruction(String target, String data)
			throws SAXException {
		// TODO Auto-generated method stub

	}

	/**
	 * 当其他某一个调用事件发生时，先调用此方法来在文档中定位。
	 * 
	 * @param locator
	 */
	public void setDocumentLocator(Locator locator) {
		// TODO Auto-generated method stub

	}

	/**
	 * 当未验证解析器忽略实体时调用此方法
	 * 
	 * @param name
	 */
	public void skippedEntity(String name) throws SAXException {
		// TODO Auto-generated method stub

	}

	/**
	 * 在解析整个文档开始时调用
	 */
	public void startDocument() throws SAXException {
		System.out.println("－－－－－开始解析XML文件－－－－－");
	}

	/**
	 * 在解析元素开始时调用
	 * 
	 * @param namespaceURI
	 * @param localName
	 * @param qName
	 * @param atts
	 */
	public void startElement(String uri, String localName, String qName,
			Attributes atts) throws SAXException {
		System.out.println("元素的开始名称－－－－－－>"+localName);
	}

	/**
	 * 在解析命名空间开始时调用
	 */
	public void startPrefixMapping(String prefix, String uri)
			throws SAXException {
		// TODO Auto-generated method stub

	}

}
