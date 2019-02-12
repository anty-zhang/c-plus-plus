package basic.compare;

import java.util.TreeSet;
/*
 * 测试Student中的Comparable比较接口
 * 每次在add的时候都会调用compareTo方法
 * 
 * 例如：如下输出结果为
 * this id: 1 compare id: 1
this id: 2 compare id: 1
this id: 2 compare id: 1
this id: 2 compare id: 2
this id: 3 compare id: 1
this id: 3 compare id: 2
[Student [id=1, name=zhangsan], Student [id=2, name=lisi], Student [id=3, name=]]
 */
public class TestComparable {

	public static void main(String[] args) {
		TreeSet <Student> ts = new TreeSet<Student> ();
		ts.add(new Student(1, "zhangsan"));
		ts.add(new Student(2, "lisi"));
		ts.add(new Student(2, "wangwu"));		// wangwu not replace lisi
		ts.add(new Student(3, ""));
		System.out.println(ts);
	}
}
