package basic.thread.poppush;

public class UnSafeStack implements IStack {
	private int index = 0;
	private int[] values =  new int[10];

	@Override
	public void push(int i) {
		values[index] = i;
		try {
			Thread.sleep(5000);
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println(i + " :push stack success");
		++index;
	}

	@Override
	public int[] pop() {
		index --;
		int[] temp = {values[index], index};
		return temp;
	}

}
