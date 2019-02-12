package designmode.abstractfactory;

public class MathProvider implements IProvider {

	@Override
	public void print() {
		System.out.println("this is math provider");
	}

}
