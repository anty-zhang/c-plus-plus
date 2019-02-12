package designmode.facade;

public class PaymentImp implements IPayment {
	@Override
	public String pay() {
		String food = "apple";
		System.out.println("payment food: " + food);
		return food;
	}
}
