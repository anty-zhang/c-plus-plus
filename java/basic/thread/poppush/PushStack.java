package basic.thread.poppush;

public class PushStack implements Runnable {
	private IStack stack;
	
	public PushStack(IStack stack) {
		this.stack = stack;
	}
	
	@Override
	public void run() {
		int i = 10;
		stack.push(i);
	}

}
