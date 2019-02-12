package designmode.singleton;

public class SingletonDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Husband b1 = Husband.newInstance();
		Husband b2 = Husband.newInstance();
		System.out.println(b1);
		System.out.println(b2);
		System.out.println(b1 == b2);
	}

}


class Husband {
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
	
	private static Husband instance = new Husband("zhangsan");
	
	private String name;
	private Husband(String name) {
		this.name = name;
	}
	
	public static Husband newInstance() {
		return instance;
	}
}