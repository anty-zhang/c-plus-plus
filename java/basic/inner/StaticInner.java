package basic.inner;

public class StaticInner {
	private int i1 = 1;
	private static int i2 = 2;
	
	public static class Inner {
		private int i3 = 3;
		private static final int i4 = 4;
		
		public void show() {
//			System.out.println("i1: " + i1);		// i1 must static
			System.out.println("i2: " + i2);
			System.out.println("i3: " + i3);
			System.out.println("i4: " + i4);
		}
	}

	public static void main(String[] args) {
		Inner i = new Inner();
		i.show();
		
		StaticInner.Inner si = new StaticInner.Inner();
		si.show();
	}
}
