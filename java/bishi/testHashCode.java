package bishi;

/*
 * 字面量hello的hashCode相同
 */

public class testHashCode {

	public static void main(String[] args) {
		String s1 = new String("hello");
		String s2 = new String("hello");
		System.out.println(s1.hashCode());
		System.out.println(s2.hashCode());
		System.out.println("hello".hashCode());
	}
}
