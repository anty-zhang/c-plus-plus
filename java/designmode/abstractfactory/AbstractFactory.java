package designmode.abstractfactory;

/*
 * 抽象工厂接口
 */

public interface AbstractFactory {
	IBook getBook();
	IProvider getProvider();
}
