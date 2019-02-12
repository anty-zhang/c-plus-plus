package basic.inner;

/*
 * 成员内部类
 * 
 */
public class MemberInner {
	private int i1 = 1;
	private static int i2 = 2;
	
	public class Inner {
		private int i3 = 3;
		private static final int i4 = 4;
		
		public void show() {
			System.out.println("i1: " + i1);
			System.out.println("i2: " + i2);
			System.out.println("i3: " + i3);
			System.out.println("i4: " + i4);
		}
	}

	public static void main(String[] args) {
		MemberInner mi = new MemberInner();
		Inner i = mi.new Inner();
		MemberInner.Inner i1 = mi.new Inner();
		i.show();
		i1.show();
	}
}
