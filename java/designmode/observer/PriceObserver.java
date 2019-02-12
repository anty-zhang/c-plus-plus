package designmode.observer;

import java.util.Observer;
import java.util.Observable;

public class PriceObserver implements Observer {

	@Override
	public void update(Observable o, Object arg) {
		System.out.println("price change: " + arg);
	}

}
