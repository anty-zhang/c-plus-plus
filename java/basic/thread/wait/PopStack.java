package basic.thread.wait;

public class PopStack implements Runnable {
	private Stack stack;
	public PopStack(Stack stack) {
		this.stack = stack;
	}
	
	@Override
	public void run() {
		for (int i = 0; i < 10; i++) {
			int [] temp = stack.pop();
			System.out.println("index: " + temp[0] 
					+ ",value: " + temp[1] + ", pop success");
		}
	}

}
