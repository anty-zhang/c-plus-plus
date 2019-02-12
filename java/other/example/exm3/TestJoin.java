package day19.high;

public class TestJoin implements Runnable{
	public void run(){
		for(int i=0;i<10;i++){
			System.out.println(Thread.currentThread().getName()+":"+i);
			try{
				Thread.sleep(400);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	public static void main(String[] args) throws InterruptedException {
		TestJoin tj1 = new TestJoin();
		Thread t1= new Thread(tj1);
		
		//t1.join();  //没有效果
		t1.start();
		
		TestJoin tj2 = new TestJoin();
		Thread t2= new Thread(tj2);
		//t1.join();  //t1执行完才执行t2和main的交互
		t2.start();
		
		t1.join();   //t1和t2之间有交互,然后才执行main
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
