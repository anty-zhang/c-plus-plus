package basic.reflect;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;


import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class TestReflectPerson {
	/*
	 * 反射实例
	 */
	public static Object getInstance(String className, Map<String, Object> map) throws Exception {
		Class<?> c = Class.forName(className);
		Object obj = c.newInstance();
		
		// 构建类信息
		Set<String> set = map.keySet();
		for (String key: set) {
			String keyName = "set" + key.substring(0, 1).toUpperCase() + key.substring(1);
			Field f = c.getDeclaredField(key);
			Method m = c.getDeclaredMethod(keyName, f.getType());
			m.invoke(obj, map.get(key));
		}
		
		return obj;
	}

	public static void main(String[] args) throws Exception {
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("name", "zhangsan");
		map.put("age", 22);
		Object obj = TestReflectPerson.getInstance("basic.reflect.Person", map);
		System.out.println(obj);
	}

}
