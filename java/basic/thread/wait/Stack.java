package basic.thread.wait;

public class Stack {
	private int index = 0;
	private int[] stack = new int[10];
	
	private boolean dataAvailable = false;	// wait notify 标识
	
	public void push(int i) {
		synchronized (this) {
			while(dataAvailable) {	
				try {
					wait();	// push线程进入等待队列
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			stack[index] = i;
			System.out.println("push index: " + index + ", value:" + i);
			index++;
			dataAvailable = true;
			this.notifyAll();		// pop线程进入锁池
		}
	}
	
	public int[] pop() {
		synchronized (this) {
			while(!dataAvailable) {
				try {
					wait();	// pop 线程进入等待队列
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			index--;
			int [] temp = {index, stack[index]};
			dataAvailable = false;
			notifyAll();		// push 线程进入锁池
			return temp;
		}
	}

}
