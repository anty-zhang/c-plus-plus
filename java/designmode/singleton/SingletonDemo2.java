package designmode.singleton;

public class SingletonDemo2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Husband2 b1 = Husband2.newInstance();
		Husband2 b2 = Husband2.newInstance();
		System.out.println(b1);
		System.out.println(b2);
		System.out.println(b1 == b2);
	}

}


class Husband2 {
	/*
	 * 1. 提供一个私有，静态本类型的类变量
	 * 		比如：private static 类名 instance = new 类名();
	 * 
	 * 2. 私有构造
	 * 
	 * 3. 提供一个公共对外接口
	 * 	比如： public static 类名 newNnstance() {}
	 * 
	 */
	
	private static Husband2 instance = null;
	
	private String name;
	private Husband2(String name) {
		this.name = name;
	}
	
	public static Husband2 newInstance() {
		if (null == instance) {
			instance = new Husband2("zhangsan");
		}
		return instance;
	}
}