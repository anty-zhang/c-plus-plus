package basic.gen;

public class testE <E extends Exception> {
	public void test(E e) {
//	public void test(E e) throws E{
		try {
			e.printStackTrace();
		} catch (Exception ee) {
//		} catch (E ee) {
			e.printStackTrace();
			ee.printStackTrace();
		}
	}
	public static void main(String[] args) {
		
	}
}
