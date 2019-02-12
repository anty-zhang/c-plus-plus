package basic;


/*1. final
 * 	1.1 修饰变量
 * 		1）局部变量和实例变量
 * 			赋值后不能改变；
 * 			修饰成员变量没有默认初始值，可在声明／构造／语句块显示赋值；	
 * 		2）修饰类变量
 * 			该变量只能始终引用一个对象，但可以改变对象的内容
 * 		3）修饰静态变量：final和static一起用表示常量；
 *
 *	1.2 修饰方法
 * 		1）final修饰方法不能被子类覆盖
 * 		2）不能修饰构造方法
 * 		3）可以重载
 * 
 * 1.3 修饰类
 * 		1）不能被继承
 * 		2）实现对象共享
 * 
 * 2. String和StringBuffer区别
 * 		String是一个final，不能被继承，因此应该这样定义
 * 			String name ＝ "zhangsan";
 * 		而不是
 * 			String name ＝ new String("zhangsan");
 * 	第一种情况：jvm会把它放到串池中，供大家分享
 * 	第二种情况：放在堆区，不能共享；
 * 
 * 	依据不变对象的特性，String对象的互相操作会造成大量垃圾对象，影响效率。
 * 	所以，在涉及大量字符串＋(连接)操作时，使用StringBuffer；
 * 
 */
public class finalTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
