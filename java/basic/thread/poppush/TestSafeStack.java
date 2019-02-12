package basic.thread.poppush;

public class TestSafeStack {

	public static void main(String[] args) {
		IStack uss = new SafeStack();
		uss.push(1);
		uss.push(2);
		
		PushStack push = new PushStack(uss);
		PopStack pop = new PopStack(uss);
		Thread t1 = new Thread(push);		// runnable 接口
		Thread t2 = new Thread(pop);
		t1.start();
		t2.start();
		/*
		 * output:
		 * 1 :push stack success
			2 :push stack success
			10 :push stack success
			index: 2 ,values: 10, pop stack success
		 */
	}

}
