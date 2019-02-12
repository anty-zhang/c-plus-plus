package bishi;

public class Super {
	static int m;
	int i = 10;

	public Super() {
		
		print();
		i = 20;
	}

	void print() {
		System.out.print("super i="+i);
	}
}
