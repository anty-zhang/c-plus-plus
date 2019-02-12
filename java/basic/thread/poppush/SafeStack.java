package basic.thread.poppush;

public class SafeStack implements IStack {

	private int index = 0;
	private int[] values = new int[20];
	
	@Override
	public void push(int i) {
		synchronized (this) {		// synchronized 实现加锁
			values[index] = i;
			try {
				Thread.sleep(5000);
			} catch (Exception e) {
				e.printStackTrace();
			}
			System.out.println(i + " :push stack success");
			++index;
		}
	}

	@Override
	public int[] pop() {
		synchronized (this) {
			index --;
			int[] temp = {values[index], index};
			return temp;
		}
	}

}
