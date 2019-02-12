package basic;
import java.math.BigDecimal;

public class TestDouble {

	public static void main(String[] args) {
		double d1 = 1.0;
		double d2 = 0.41;
		System.out.println(d1 - d2);		// 0.5900000000000001
		
		BigDecimal bd1 = new BigDecimal(d1);
		BigDecimal bd2 = new BigDecimal(d2);
		double d = bd1.subtract(bd2).doubleValue();
		System.out.println(d);			// 0.5900000000000001
		
		BigDecimal bd3 = new BigDecimal(d1 + "");
		BigDecimal bd4 = new BigDecimal(d2 + "");
		double dd = bd3.subtract(bd4).doubleValue();
		System.out.println(dd);			// 0.59
		
		BigDecimal bd5 = new BigDecimal("1");
		BigDecimal bd6 = new BigDecimal("3");
		double ddd = bd5.divide(bd6, 10,BigDecimal.ROUND_HALF_UP).doubleValue();
		System.out.println(ddd);		// 0.3333333333
		
		/*
		 1/2=0.5  no 1/2=0.5000000000
		 
		 */
		
		BigDecimal b1 = new BigDecimal(1.0+"");
		BigDecimal b2 = new BigDecimal(4.0+"");
		try{
			System.out.println("try"+b1.divide(b2));
		}catch(Exception e){
			System.out.println("catch"+b1.divide(b2,10,BigDecimal.ROUND_HALF_UP).doubleValue());
		}
		
	}

}
