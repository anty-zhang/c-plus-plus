package bishi;
import java.text.ParseException;
import java.text.SimpleDateFormat;

public class TestDate {

	public static void main(String[] args) throws ParseException {
		// TODO Auto-generated method stub
//		String s1 = "2009-08-16 0:0:0";
//		String s2 = "2009-09-16 0:0:0";
		
//		String s1 = "20090816 0:0:0";
//		String s2 = "20090916 0:0:0";
		
		String s1 = "20090816";
		String s2 = "20090916";
		
		System.out.println(TestDate.getDate(s2, s1)/(24*60*60));
	}
	
	public static long getDate(String date1, String date2) throws ParseException {
		SimpleDateFormat sdf1 = new SimpleDateFormat("yyyyMMdd");
		SimpleDateFormat sdf2 = new SimpleDateFormat("yyyyMMdd");
		System.out.println("test getTime: " + sdf1.parse(date1).getTime());
		long l = (sdf1.parse(date1).getTime() 
				- sdf2.parse(date2).getTime()) / 1000;
		return l;
	}

}
