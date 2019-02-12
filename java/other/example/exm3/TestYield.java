package day19.high;

public class TestYield implements Runnable {

	public void run() {
		for(int i=0;i<10;i++){
			System.out.println(Thread.currentThread().getName()+":"+i);
			try{
				//Thread.sleep(400);
				Thread.yield();
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}

	public static void main(String[] args) {
		TestYield ty1 = new TestYield();
		Thread t1 = new Thread(ty1);
		t1.setPriority(9);
		t1.start();
//		
//		TestYield ty2 = new TestYield();
//		Thread t2 = new Thread(ty2);
//		t1.setPriority(1);
//		t2.start();
		
		
		for(int i=0;i<10;i++){
			System.out.println("main:"+i);
			try{
				//Thread.sleep(400);
				Thread.yield();
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}

}
