package basic.thread.wait;

public class TestWaitStack {

	public static void main(String[] args) {
		Stack stack = new Stack();
		PushStack push = new PushStack(stack);
		PopStack pop1 = new PopStack(stack);
		PopStack pop2 = new PopStack(stack);
		
		Thread t1 = new Thread(push);
		Thread t2 = new Thread(pop1);
		Thread t3 = new Thread(pop2);
		t1.start();
		t2.start();
		t3.start();
	}

}
