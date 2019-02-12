package basic.property;

import java.util.Properties;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class TestProperty {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Properties p = new Properties();		// Properties
		FileInputStream fis = new FileInputStream("/Users/guoqiangzhang/Documents/workspace/mytest/src/basic/property/db.xml");
		p.load(fis);						// load
		fis.close();
		
		String db = p.getProperty("db");
		String name = p.getProperty("name");
		String pwd = p.getProperty("password");
		System.out.println("db: " + db + " ,name:" + name + " ,pwd:" + pwd);
		
		p.setProperty("db", "mytest1");		// set property
		FileOutputStream fos = new FileOutputStream("/Users/guoqiangzhang/Documents/workspace/mytest/src/basic/property/db.xml");
		p.store(fos, "zhangguoqiang1");		// store	
	}
}
