package basic.thread.example;

/*
 * 一个线程打印数：1-52，另一个线程打印字母：A－Z。
 * 要求格式：12A34B...5152Z.
 * 采用进程间通信完成，不可造成死锁
 */
public class TestThread {
	
	public static void main(String[] args) {
		Object obj = new Object();
		ThreadA ta = new ThreadA(obj);
		ThreadB tb = new ThreadB(obj);
		ta.start();
		tb.start();
	}

}
