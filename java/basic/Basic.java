package basic;

public class Basic {
	
	/*
	 * 测试Integer
	 */
	public static void testInteger() {
		Integer i1 = 129;
		Integer i2 = 129;
		int i3 = i1+i2;
		//i1++;
		Integer i4 = 258;
		System.out.println(i1==i2);  // false 包装类型比较为Integer类型
		System.out.println(i3==i4);  // Integer和int类型比较为int类型
		System.out.println(i4==i3);
		byte b = 3;
		Byte b1 = 127;
		long l = 3;
		
		//Long l1 =3;//(long)3;3L
//		Double d = 3;//3d;//3.0; //×Ô¶¯×°Ïä³ÉIngeger
	}

	public static void main(String[] args) {
		Basic.testInteger();
	}

}
