package basic.anonymous;

public class B {
	public IA back() {
		return new IA() {
			public void print() {
				System.out.println("class b implements A print func");
			}
		};
	}
}
