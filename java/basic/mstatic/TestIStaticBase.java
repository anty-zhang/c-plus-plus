package basic.mstatic;

public class TestIStaticBase extends IStaticBase {
	@Override
	void method() {
		System.out.println("method for TestIStaticBase");
	}
	
	// @Orverride error
	static void staticMehthod() {
		System.out.println("staticMehtod for TestIStaticBase");
	}
	
	public static void main(String[] args) {
		/*
		 * isb.staticMethod();
		 * 如果父类中有静态和非静态同名函数，那么对象.函数名，首先会调用类中的非静态函数
		 */
		IStaticBase isb = new IStaticBase();
		isb.method();				// base's method
		isb.staticMethod();			// base's static method
		
		
		TestIStaticBase tsb = new TestIStaticBase();
		tsb.method();				// method for TestIStaticBase
		tsb.staticMehthod();			// staticMehtod for TestIStaticBase
	}
}
