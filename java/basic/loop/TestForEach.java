package basic.loop;

import java.util.Set;
import java.util.HashSet;

public class TestForEach {
	public static void main(String[] args) {
		Set<String> s = new HashSet<String> ();
		s.add("a");
		s.add("b");
		s.add("c");
		s.add("z");
		
		for (String ss: s) {			// for each
			System.out.print(ss);
		}
	}
}
