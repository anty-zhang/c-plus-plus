package basic.enumt;

public final class Deng {		// final class
	public static final Deng RED = new Deng("red");		// static final
	public static final Deng GREEN = new Deng("green");
	public static final Deng YELLOW = new Deng("yellow");
	
	private Deng(String s) {		// private constructor
		System.out.println(s);
	}
	
	public static Deng[] getAll() {
		Deng [] d = {RED, GREEN, YELLOW};
		return d;
	}
}
