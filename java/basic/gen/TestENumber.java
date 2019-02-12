package basic.gen;

import java.util.List;

public class TestENumber <E extends Number & Comparable>{
	public void test(Number num) {
		//num.compareTo(num);//The method compareTo(Number) is undefined for the type Number
		System.out.println(num.intValue());
	}
	
	public void test1(E e) {
		System.out.println(e.compareTo(e));  //0
		System.out.println(e.intValue());    //8
	}
	public void test2(List<? extends Number> list){
		
	}
	public static void main(String[] args) {
		TestENumber<Integer> tn = new TestENumber<Integer>();
		tn.test1(8);
	}

}
