package basic.thread.wait;

import java.util.Random;

public class PushStack implements Runnable {
	private Stack stack;
	
	public PushStack(Stack stack) {
		this.stack = stack;
	}
	
	@Override
	public void run() {
		Random r = new Random();
		for (int i = 0; i < 10; i ++) {
			int ran = r.nextInt(50) + 1;
			stack.push(ran);
		}
	}

}
