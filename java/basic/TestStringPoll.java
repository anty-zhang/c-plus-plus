package basic;

public class TestStringPoll {

	public static void main(String[] args) {
		String s1 = "abc";//1
		String s2 = "abc";//1
		String s3 = new String("bcd");  //3
		String s4 = new String("bcd");  //4
		System.out.println(s1==s2); //true
		System.out.println(s3==s4); //false
		System.out.println("s1.hashCode():"+s1.hashCode());
		System.out.println("s2.hashCode():"+s2.hashCode());
		System.out.println("s3.hashCode():"+s3.hashCode());
		System.out.println("s4.hashCode():"+s4.hashCode());
		
		String s5 = "abcd";
		String s6 = "abc"+"d";
		String s7 = s1+"d";
		String s8 = s1+"d";
		System.out.println(s5==s6); //true
		System.out.println(s5==s7); //false  ***********
		System.out.println(s6.equals(s7));  // true
		System.out.println("s6.hashCode():"+s6.hashCode());
		System.out.println("s7.hashCode():"+s7.hashCode());
		System.out.println(s7==s8);// false
	}

}
