package basic.compare;

import java.util.TreeSet;
import java.util.Comparator;

/*
 * 对象的两种比较方式的实现
 * Comparator
 * 
 * 如下实例输出结果：
 * id1: 1 ,id2: 1
id1: 2 ,id2: 1
id1: 2 ,id2: 1
id1: 2 ,id2: 2
id1: 3 ,id2: 1
id1: 3 ,id2: 2
[Student [id=3, name=], Student [id=2, name=lisi], Student [id=1, name=zhangsan]]
====================================
id1: 1 ,id2: 1
id1: 2 ,id2: 1
id1: 3 ,id2: 1
id1: 4 ,id2: 1
id1: 4 ,id2: 3
id1: 5 ,id2: 3
id1: 5 ,id2: 4
id1: 6 ,id2: 3
id1: 6 ,id2: 4
id1: 6 ,id2: 5
id1: 7 ,id2: 3
id1: 7 ,id2: 5
id1: 7 ,id2: 6
id1: 8 ,id2: 3
id1: 8 ,id2: 5
id1: 8 ,id2: 6
id1: 8 ,id2: 7
[Student [id=1, name=a], Student [id=3, name=d], Student [id=4, name=e], Student [id=5, name=g], Student [id=6, name=h], Student [id=7, name=k], Student [id=8, name=z]]

 * 
 */

public class TestComparator {

	public static void main(String[] args) {
		TreeSet<Student> ts = new TreeSet<Student>(
				new Comparator<Student> () {
					public int compare(Student s1, Student s2) {
						System.out.println("id1: " + s1.getId() + " ,id2: " + s2.getId());
						return s2.getId() - s1.getId();
					}
				});
		
		ts.add(new Student(1, "zhangsan"));
		ts.add(new Student(2, "lisi"));
		ts.add(new Student(2, "wangwu"));		// wangwu not replace lisi
		ts.add(new Student(3, ""));
		System.out.println(ts);
		
		System.out.println("====================================");
		
		TreeSet <Student> ts1 = new TreeSet<Student> (new Comparator<Student>() {
			public int compare(Student s1, Student s2) {
				System.out.println("id1: " + s1.getId() + " ,id2: " + s2.getId());
				return s1.getName().compareTo(s2.getName());
			}
		});
		
		ts1.add(new Student(1,"a"));
		ts1.add(new Student(2,"a"));
		ts1.add(new Student(3,"d"));
		ts1.add(new Student(4,"e"));
		ts1.add(new Student(5,"g"));
		ts1.add(new Student(6,"h"));
		ts1.add(new Student(7,"k"));
		ts1.add(new Student(8,"z"));
		System.out.println(ts1);
	}

}
