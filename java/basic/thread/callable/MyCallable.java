package basic.thread.callable;

import java.util.concurrent.Callable;

/*
 * Callable和Runnable接口类似，其中Callable产生结果，Future拿到结果
 * Future可以拿到异步程序的返回值
 */

public class MyCallable implements Callable<String> {
	private int state;
	public MyCallable(int state) {
		this.state = state;
	}
	@Override
	public String call() throws Exception {
		if (state == 1) {
			return "ok";		// 返回字符串
		} else if ( state == 2) {
			while(true) {	// 死循环
				System.out.println("super");
				Thread.sleep(10);
			}
		} else {
			throw new Exception("test");	// 抛出异常
		}
	}

}
