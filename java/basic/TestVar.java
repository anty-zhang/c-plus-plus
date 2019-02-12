package basic;

/*
 * 测试可变入参
 */
public class TestVar {
	public void test(String... s) {
		System.out.println("public void test (String.. s): " + s);
	}
	
	public void test(String s) {
		System.out.println("pulic void test(String s): " + s);
	}
	
	public void test(String s, String... s1) {
		System.out.println("public void test(String s, String... s1)s :" + s + " ,s1: " + s1); 
	}
	
	public static void main(String[] args) {
		TestVar t = new TestVar();
		t.test("a");		// pulic void test(String s): a
//		t.test("a", "b");		// compile error
		t.test(new String [] {"a", "b"});	// public void test (String.. s): [Ljava.lang.String;@1cb52598
		t.test("a", new String[] {"c", "d"}); // public void test(String s, String... s1)s :a ,s1: [Ljava.lang.String;@38b72ce1
		t.test();	// public void test (String.. s): [Ljava.lang.String;@1e384de
		t.test(args);	// public void test (String.. s): [Ljava.lang.String;@280bca
		t.test("", args);  // public void test(String s, String... s1)s : ,s1: [Ljava.lang.String;@280bca
	}

}
