package designmode.facade;

public class CookImp implements ICook {

	@Override
	public String cook(String food) {
		System.out.println("cook food: " + food);
		return food;
	}

}
