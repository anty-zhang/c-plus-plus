package io.serializable.exp;

import java.io.*;

/*
 * ObjectOutputStream 流持久化对象
 */

public class TestPersonSerializable {
	public static void seriaPerson() throws Exception {
		FileOutputStream fos = new FileOutputStream("./src/io/serializable/exp/seria.txt");
		ObjectOutputStream oos = new ObjectOutputStream(fos);
		Person p = new Person("zhangsan", 22, "man", new Object());
		oos.writeObject(p);
	}
	
	public static void unSeriaPerson() throws Exception {
		FileInputStream fis = new FileInputStream("./src/io/serializable/exp/seria.txt");
		ObjectInputStream ois = new ObjectInputStream(fis);
		Object obj = ois.readObject();
		System.out.println(obj);
	}
	
	public static void main(String[] args) throws Exception {
		TestPersonSerializable.seriaPerson();
		TestPersonSerializable.unSeriaPerson();
		
	}

}
