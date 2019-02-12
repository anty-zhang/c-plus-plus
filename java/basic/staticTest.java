package basic;

/*1. static
 * 	static池化思想：把需要共享的数据放在池中（节省空间，共享数据，常驻内存）
 * 	1.1 修饰属性
 * 		在类加载时创建并初始化，类加载过程只进行一次；
 * 		可以在静态方法中使用，也可以在非静态方法中使用；
 * 
 * 	1.2 修饰方法
 * 		只有类的概念，没有对象概念，所以不能出现this关键词；
 * 		静态方法中只能访问静态属性（不能访问非静态成员－－属性和方法），但可通过组合方式访问本类中非静态属性和方法；
 * 		例如：
 * 			public class Test{
			private static int testnum;
			public int testage;
			public static int test（）{
					testnum++;
				Test t=new Test();
				t.testage；    //组合方式
				
			}
		} 
 * 		静态方法可以被覆盖，但是没有多态。所有java虚拟机对于静态方法的选择，看编译时的类型
 * 			而不是运行时类型；
 * 		父类静态方法只能又子类静态方法覆盖，非静态方法也只能由非静态方法覆盖；
 * 		
 * 	1.3 修饰类
 * 
 * 	1.4 修饰代码块
 * 		代码块只在类加载时执行一次，因此静态代码块一定放在类里面，但不能是任何方法的里面；
 * 		可用静态初始代码块初始化一个类；
 * 		
 * 
 */
public class staticTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
