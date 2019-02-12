package collect.list;
import java.util.Scanner;
import java.util.List;
import java.util.LinkedList;
import java.util.Iterator;
import java.util.Set;
import java.util.HashSet;

/*
 * 1. 范型使用
 * 2. instanceof使用
 * 3. toString方法使用
 * 4. Iterator 使用
 */

public class Input {
	
	private static Scanner sc;

	public static void show1() {
		sc = new Scanner(System.in);
		 List list = new LinkedList();
		
		while(true) {
			System.out.println("input name,id,sal");
			String t = sc.nextLine();
			if ("over".equals(t)) {
				System.out.println("stop");
				break;
			}
			
			String [] m = t.split(",");
			if (list.size() != 3) {
				if (m[2].matches("^\\d+[.]?\\d*$")) {
					double d = Double.parseDouble(m[2]);
					Emp e = new Emp(m[0], m[1], d);
					list.add(e);
				}
			}
		}
		System.out.println("stop");
		
		System.out.println("bengin print the list content");
		System.out.println("list size:" + list.size());
		for (int i = 0; i < list.size(); i++) {
			Object obj = list.get(i);
			
			if (obj instanceof Emp) {		// instanceof
				Emp em = (Emp)obj;
//				System.out.println(em);		// call toString of function
				
				if (em.getName().startsWith("z")) {
					System.out.println(em.toString());	// direct call toString of function
				}
			}
		}
		
		System.out.println("end print the list content");
	}
	
	public static void show2() {
		sc = new Scanner(System.in);
		List<Emp> list = new LinkedList<Emp>();		// 使用范型
		
		while(true) {
			System.out.println("input name,id,sal");
			String t = sc.nextLine();
			if ("over".equals(t)) {
				System.out.println("stop");
				break;
			}
			
			String [] m = t.split(",");
			if (list.size() != 3) {
				if (m[2].matches("^\\d+[.]?\\d*$")) {
					double d = Double.parseDouble(m[2]);
					Emp e = new Emp(m[0], m[1], d);
					list.add(e);
				}
			}
		}
		System.out.println("stop");
		
		System.out.println("bengin print the list content");
		System.out.println("list size:" + list.size());
		for (int i = 0; i < list.size(); i++) {
			Emp emp = list.get(i);		// 使用范型可以不用instanceof 判断类型
			if (emp.getName().startsWith("z")) {
				System.out.println(emp.toString());	// direct call toString of function
			}
		}
		
		System.out.println("end print the list content");
	}
	
	public static void testIteratorFunc() {
		Set<Integer> set = new HashSet<Integer>();
		set.add(2);
		set.add(3);
		set.add(5);
		set.remove(23);
		set.add(new Integer(6));
		set.add(23);
		
		System.out.println("set size: " + set.size());
		System.out.println("set is:" + set);
		Iterator<Integer> i = set.iterator();
		while(i.hasNext()) {
			Integer ii = i.next();
			System.out.println("ii is: " + ii);
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Input.show1();
		Input.testIteratorFunc();
	}
}
