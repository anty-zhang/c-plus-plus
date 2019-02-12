package designmode.observer;

/*
 * 观察者模式
 */
public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Product p = new Product();
		PriceObserver po = new PriceObserver();
		p.addObserver(po);		// add observer
		p.setPrice(200.9);
		System.out.println("test main last");
	}

}
