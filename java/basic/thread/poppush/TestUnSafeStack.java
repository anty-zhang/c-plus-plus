package basic.thread.poppush;

public class TestUnSafeStack {

	public static void main(String[] args) {
		UnSafeStack uss = new UnSafeStack();
		uss.push(1);
		uss.push(2);
		
		PushStack push = new PushStack(uss);
		PopStack pop = new PopStack(uss);
		Thread t1 = new Thread(push);		// runnable 接口
		Thread t2 = new Thread(pop);
		t1.start();
		t2.start();
		
		/*没有加锁导致输出错误
		 * output:
		 * 1 :push stack success
			2 :push stack success
			index: 1 ,values: 2, pop stack success
			10 :push stack success

		 * 
		 */
	}

}
