package basic.thread.example;

public class ThreadB extends Thread {
	private Object obj;
	public ThreadB(Object o) {
		this.obj = o;
	}
	
	@Override
	public void run() {
		synchronized (obj) {
			for (char c = 'A'; c <= 'Z'; c++) {
				System.out.print(c);
				obj.notifyAll();				// notify
				
				try {
					if (c != 'Z') {
						obj.wait();			// wait
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
}
