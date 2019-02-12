package day19.high;

public class TestRunnable implements Runnable {

	public void run() {
		for(int i=0;i<10;i++){
			System.out.println("run:"+i);
			try{
				Thread.sleep(1000);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	public static void main(String[] args){
		TestRunnable tr = new TestRunnable();
		Thread t = new Thread(tr);
		t.start();
		for(int i=0;i<10;i++){
			System.out.println("main:"+i);
			try{
				Thread.sleep(500);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
}
