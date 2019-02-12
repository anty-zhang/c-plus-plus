package collect;

import java.util.Map;
import java.util.HashMap;
import java.util.Set;

public class TestHashMap {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<String, Integer> m = new HashMap <String, Integer>();
		m.put("a", 1);
		m.put("b", 2);
		m.put("c", 3);
		m.remove("b");
		m.remove("b");
		
		Set<String> s = m.keySet();
		for (String key: s) {
			Integer value = m.get(key);
			System.out.println("key: " + key + " ,value: " + value);
		}
		
		Set ss = m.entrySet();
		System.out.println(ss);	// [c=3, a=1]
	}
}
