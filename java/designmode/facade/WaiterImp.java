package designmode.facade;

public class WaiterImp implements IWaiter {

	@Override
	public void serve(String food) {
		System.out.println("waiter serve food: " + food);
	}

}
