package basic;

public class TestTry {

	public static void main(String[] args) {
		int a = 2;
		int b = 0;
		try{
			System.out.println("begin");
			a = a/b;
			System.out.println("try");
		}catch(ArithmeticException e){
			e.printStackTrace();  
			System.out.println("catch");
		}finally{
			System.out.println("finally");
		}
		System.out.println("main");	
	}

}
