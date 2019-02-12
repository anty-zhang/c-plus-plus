package basic.gen;
import java.util.List;

public class TestEMethod <G> {
	public G test1(G g) {
		System.out.println("test1 g: " + g);
		return g;
	}
	
	public Object test2(Object obj) {
		System.out.println("test2 obj: " + obj);
		return obj;
	}
	
	public void test3(List <? extends Number> list) {
	// public void test3(List<E extends Number> list) {
		
	}
	public static void main(String[] args) {
		TestEMethod <String> tm = new TestEMethod<String> ();
		String s1 = tm.test1("zhangsan");
		Object obj = tm.test2("lisi");
		System.out.println(s1);
		System.out.println(obj);
		
		TestEMethod<Integer> tem1 = new TestEMethod<Integer>();
		Integer i1 = tem1.test1(11);
		Object i2 = tem1.test2(11);
		System.out.println(i1);
		System.out.println(i2);

	}

}
