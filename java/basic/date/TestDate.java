package basic.date;

import java.util.Date;
import java.util.Calendar;


public class TestDate {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Date d1 = new Date();
		Calendar d2 = Calendar.getInstance();
		Date d3 = d2.getTime();
		
		d2.set(2016, 02, 16);
		Date d4 = d2.getTime();
		
		System.out.println(d1);
		System.out.println(d2);
		System.out.println(d3);
		System.out.println(d4);
		
	}

}
