package bishi;

public class TestInt {
	public static void main(String[] args) {
		byte b=12;
		//byte b2=129;// ³¬³öÁË·¶Î§
		char c='a';
		String c2="a";

		int i1=c;
		//int i2=c2; //×Ö·û¿ÉÒÔ¸³Öµ¸øint£¬µ«ÊÇString²»ÄÜ
		int i3=12;

		long l1=129;//¿ÉÒÔ×ª»»
		long l2=129L;
		long l3=i3;//int ¿ÉÒÔ×ª»»long
		System.out.println("i1: "+i1);
		System.out.println("l1: "+l1);
		System.out.println("l2: "+l2);
		System.out.println("l3: "+l3);
	}
}
