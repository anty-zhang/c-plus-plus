package basic.thread.callable;

import java.util.concurrent.*;

public class TestMyCallable {

	public static void main(String[] args) throws Exception {
		ExecutorService es = Executors.newFixedThreadPool(3);
		Future f1 = es.submit(new MyCallable(1));
		Future f2 = es.submit(new MyCallable(2));
		Future f3 = es.submit(new MyCallable(3));
		
		System.out.println(f1.get());
		System.out.println(f2.cancel(true));
		try {
			System.out.println("f3:" + f3.get());
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		es.shutdown();
	}

	/*
	 * super
ok
true
java.util.concurrent.ExecutionException: java.lang.Exception: test
	at java.util.concurrent.FutureTask.report(FutureTask.java:122)
	at java.util.concurrent.FutureTask.get(FutureTask.java:188)
	at basic.thread.callable.TestMyCallable.main(TestMyCallable.java:16)
Caused by: java.lang.Exception: test
	at basic.thread.callable.MyCallable.call(MyCallable.java:25)
	at basic.thread.callable.MyCallable.call(MyCallable.java:1)
	at java.util.concurrent.FutureTask.run(FutureTask.java:262)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	at java.lang.Thread.run(Thread.java:745)

	 */
}
