package designmode.facade;

public class Customer {
	public void haveDinner() {
		Facade f = new Facade();
		f.serve();
	}
}
