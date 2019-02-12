package basic.thread.example;

public class ThreadA extends Thread {
	private Object obj;
	public ThreadA(Object o) {
		this.obj = o;
	}
	
	@Override
	public void run() {
		synchronized (obj) {
			for (int i = 1; i <= 26; i++) {
				System.out.print(i*2 - 1);
				System.out.print(i*2);
				obj.notifyAll();					// notify
//				System.out.println("i: " + i);
				try {
					if (i != 26) {
//						System.out.println("wait before");
						obj.wait();				// wait 释放所有锁，进入等待队列
//						System.out.println("wait after");
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
}
