package abstractexample;

/*abstract修饰类和方法
 * 1.抽象类
 * 	1.1 抽象类不可以生成对象（但可以有构造方法留给子类使用），必须被继承使用
 * 	1.2	抽象类可以声明作为编译时的类型，但不能作为运行时类型
 * 	1.3	abstract不能和private，static，final同时出现
 * 	1.4 抽象类的设计模式：模版方法
 * 	1.5	抽象类中不一定有抽象方法，但有抽象方法的类一定是抽象类
 */
public class abstractTest {
	public static void main(String []args){
		XiaoPin x1 = new ShuoShi();
		XiaoPin x2 = new DaPuKe();
		x1.act();
		x2.act();
		
	}
}
