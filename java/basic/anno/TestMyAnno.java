package basic.anno;
import java.lang.reflect.Method;

/*
 * 注解稍后研究
 */
public class TestMyAnno {
	
	@MyAnnotation(name="zhangsan", age=22)
	public void test() {
		System.out.println("hello test");
	}

	public static void main(String[] args) {
		Class<?> c = TestMyAnno.class;
		Method [] mt = c.getDeclaredMethods();
		
		for (Method m: mt) {
			System.out.println(m);
			if (m.isAnnotationPresent(MyAnnotation.class)) {
				MyAnnotation mya = m.getAnnotation(MyAnnotation.class);
				System.out.println(mya);		// @basic.anno.MyAnnotation(name=zhangsan, age=22)
				System.out.println(mya.name());
				System.out.println(mya.age());
			}
		}
		
	}

}
