package designmode.abstractfactory;

public class EnglishFactory implements AbstractFactory {

	@Override
	public IBook getBook() {
		// TODO Auto-generated method stub
		return new EnglishBook();
	}

	@Override
	public IProvider getProvider() {
		// TODO Auto-generated method stub
		return new EnglishProvider();
	}

}
