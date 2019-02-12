package designmode.abstractfactory;

public class MathFactory implements AbstractFactory {

	@Override
	public IBook getBook() {
		return new MathBook();
	}

	@Override
	public IProvider getProvider() {
		return new MathProvider();
	}

}
