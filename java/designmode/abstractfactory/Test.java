package designmode.abstractfactory;
/*
 * 接口抽象工厂实例
 * 		AbstractFactory
 * 			EnglishFactory
 * 			MathFactory
 * 		IBook
 * 			EnglishBook
 * 			MathBook
 * 		IProvider
 * 			EnglishProvider
 * 			MathProvider
 * 
 */
public class Test {

	public static void main(String[] args) {
		AbstractFactory af = new MathFactory();
		IBook ib = af.getBook();
		IProvider ip = af.getProvider();
		ib.print();
		ip.print();
	}

}
