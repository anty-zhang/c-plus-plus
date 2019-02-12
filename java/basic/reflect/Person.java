package basic.reflect;

public class Person {
	private String name;
	private int age;
	
	public Person() {
		super();
	}
	
	// 使用自定义异常
	public Person(String name, int age) throws AgeException {
		super();
		this.setName(name);
		this.setAge(age);
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
	
	// 使用自定义异常
	public void setAge(int age)  throws AgeException {
		if (0 < age && age < 150) {
			this.age = age;
		} else {
			throw new AgeException("too large age: " + age);
		}
	}
	
	@Override
	public String toString() {
		return "name: " + getName() + " ,age: " + getAge();
	}
	
	public static void main(String [] args) {
		/*
		 * 测试自定义异常
		 */
		try {
			Person p = new Person("zhangsna", 200);
		} catch (AgeException e){
			e.printStackTrace();
		}
	}
}
