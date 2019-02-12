package day19.high;

public class FirstThread extends Thread{

	@Override
	public void run(){
		for(int i=0;i<10;i++){
			System.out.println("run:"+i);
			try{
				Thread.sleep(1000);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	public static void main(String[] args) {
		FirstThread ft = new FirstThread();
		ft.start();
		for(int i=0;i<10;i++){
			System.out.println("main:"+i);
			try{
				Thread.sleep(10);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
}
