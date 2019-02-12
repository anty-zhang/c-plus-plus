package bishi;

public class TestExtends extends Super{
	int j = 30;
	public TestExtends(){
		//
		print();
		j = 40;
		print();
	}
	

	void print(){
		System.out.println("sub j = "+j);
	}

	public static void main(String[] args) {
		//System.out.println(new TestExtends().j);
		Super t  = new TestExtends();
		TestExtends tt = (TestExtends)t;
	}

}
