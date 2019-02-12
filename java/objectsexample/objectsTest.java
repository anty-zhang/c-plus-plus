package objectsexample;

/*
 * Object 类中默认三个方法：
 * 1. finalize(): 垃圾回收时由JVM调用
 * 2. toString(): 将一个对象以字符串形式返回
 * 3. equal(): 判断对象值是否相等
 *  
 */

public class objectsTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	
	下面是覆盖 equals 方法的标准流程:
		public Boolean equals(Object o){ /**第一步:现判断两个对象地址是否相等*/
		if(this = = o) return true;
		/**第二步:如果参数是 null 的话直接返回 false;*/ if(o = = null) return false;
	
		/**第三步:如果两个对象不是同一个类型直接返回 false*/
		if( !(o instanceof Student) ) return false;
		/**第四步:将待比较对象强转成指定类型,然后自定 义比较规则*/
		Student s = (Student)o; 
		If(s.name.equals(this.name)&&s.age==this.age)
		return true;
		else return false }

}
