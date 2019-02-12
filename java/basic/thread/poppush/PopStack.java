package basic.thread.poppush;

public class PopStack implements Runnable {
	
	private IStack stack;
	
	public PopStack(IStack stack) {
		this.stack = stack;
	}
	
	@Override
	public void run() {
		int [] temp = stack.pop();
		System.out.println("index: " + temp[1] 
				+ " ,values: " + temp[0] 
						+ ", pop stack success");
	}

}
