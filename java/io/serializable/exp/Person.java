package io.serializable.exp;

import java.io.Serializable;

/*
 * 持久化Person对象
 */
public class Person implements Serializable {
	private static final long seriaVersionUID = 1L;
	private String name;
	private transient int age; // transient 修饰属性不被持久化
	private String sex;
//	private Object obj; // Object持久化异常
	private static Object obj;		// static not Serializable
	
	public Person() {
		super();
	}
	
	public Person(String name, int age, String sex, Object obj) {
		super();
		this.setName(name);
		this.setAge(age);
		this.setSex(sex);
		this.setObj(obj);
	}
	
	@Override
	public String toString() {
		return "Person [name=" + name + ", age=" + age + ", sex=" + sex + "]";
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public static Object getObj() {
		return obj;
	}
	public static void setObj(Object obj) {
		Person.obj = obj;
	}
	
}
