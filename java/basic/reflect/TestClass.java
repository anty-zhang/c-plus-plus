package basic.reflect;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class TestClass {
	public static void testClass () throws ClassNotFoundException {
		Class c1 = Class.forName("java.lang.String");	// class java.lang.String
		Class c2 = String.class;		// class java.lang.String
		Class c3 = "ab".getClass();		// class java.lang.String
		
		Class c4 = int.class;		// int
		Class c5 = Integer.TYPE;		// int
		Class c6 = Integer.class;	// class java.lang.Integer
		Integer i7 = 7;
		Class c7 = i7.getClass();
		System.out.println(c1 == c2);	// true
		System.out.println(c2 == c3);	// true
		
		System.out.println(c4 == c5);	// true
		System.out.println(c5 == c6);	// false
		System.out.println(c6 == c7);	// true
	}
	
	/*
	 * 反射测试构造函数
	 * 1. getConstructor：只能访问类中声明的public的构造函数
	 * 2. getDeclaredConstructor：访问类中所有构造方法
	 */
	public static void testConstructor() throws Exception {
		Class<?> c = Class.forName("basic.reflect.Person");
		Object obj = c.newInstance();
		Constructor<?> con = c.getConstructor(String.class, int.class);
		Object obj1 = con.newInstance("zhangsan", 20);
				
		System.out.println(c);	// class basic.reflect.Person
		System.out.println(obj); // name: null ,age: 0
		System.out.println(obj1); // name: zhangsan ,age: 20
	}

	public static void testInstance() throws Exception {
		Class<?> c = Class.forName("java.lang.String");
		Object o = c.newInstance();
		System.out.println("==" + o); // ==
		
		Class<?> c1 = Class.forName("basic.reflect.TestClass");
		Object o1 = c1.newInstance();
		System.out.println("==" + o1); // ==basic.reflect.TestClass@39fc0f04
	}
	
	/*
	 * 测试Field
	 */
	public static void testField() throws Exception {
		Class<?> c = Person.class;
		Object obj = c.newInstance();
		System.out.println(obj);		// name: null ,age: 0
		
		Field f = c.getDeclaredField("age");
		f.setAccessible(true); // 访问私有变量
		f.set(obj, 20);
		System.out.println(obj);		// name: null ,age: 20
		
	}
	
	
	/*
	 * 测试Method
	 * 1. getMethod：只能访问类中声明的公有方法，不能访问私有方法。
	 * 			能访问从其他类中继承来的公有方法。
	 * 2.getDeclaredMethod：能访问类中所有方法。
	 * 			不能访问从其他类中继承来的方法
	 */
	public static void testMethod() throws Exception{
//		Class<?> c = Person.class;
		Class<?> c = Class.forName("basic.reflect.Person");
		Object o = c.newInstance();
		Method m = c.getMethod("setAge", int.class);
		m.invoke(o, 22);
		// testMethod obj: name: null ,age: 22
		System.out.println("testMethod obj: " + o);
		
	}
	
	
	/*
	 * test declare
	 * 1. getFields: 只访问公有字段，不能访问私有字段。
	 * 			能访问从其他类继承来的公有方法。
	 * 2.getDeclaredFields：访问所有字段（和private，public，protected无关）
	 * 			不能访问从其他类继承来的方法
	 * 
	 */
	
	public static void TestDeclare() throws Exception {
		Class<?> c = Person.class;
		Field [] f1 = c.getFields();
		Field [] f2 = c.getDeclaredFields();
		
		for(Field f: f1) {
			System.out.println(f);
		}
		System.out.println("=============1==============");
		for (Field f: f2) {
			System.out.println(f);
		}
		System.out.println("=============2==============");
		
		Method [] m1 = c.getMethods();
		Method [] m2 = c.getDeclaredMethods();
		for(Method m: m1) {
			System.out.println(m);
		}
		System.out.println("=============3==============");
		for(Method m: m2) {
			System.out.println(m);
		}
		
	}
	
	public static void main(String[] args) throws Exception {
//		TestClass.testClass();
//		TestClass.testConstructor();
//		TestClass.testInstance();
//		TestClass.testField();
//		TestClass.testMethod();
		TestClass.TestDeclare();
		
	}

}
