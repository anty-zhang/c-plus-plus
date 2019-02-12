package basic.inner;

/*
 * 函数内部类
 */
public class LocalInner {
	private int i1 = 1;
	private static int i2 = 2;
	
	public void test() {
//		public int i3 = 3; 	// public error
		int i3 = 3;
		final int i4 = 4;
		
//		public class Inner {  // public error
		class Inner {
			public void test(int i5) {
				System.out.println("i1: " + i1);
				System.out.println("i2: " + i2);
//				System.out.println("i3: " + i3);  // i3 must be final
				System.out.println("i4: " + i4);
				System.out.println("i5: " + i5);
			}
		}
		
		Inner i = new Inner();
		i.test(5);
	}
	
	public static void main(String []args) {
		LocalInner l = new LocalInner();
		l.test();
	}
}
