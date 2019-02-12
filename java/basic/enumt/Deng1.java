package basic.enumt;

public enum Deng1 {
	RED("red"), GREEN("green"), YELLOW("yellow");
	Deng1(){}
	Deng1(String s){
		System.out.println("Deng1 s: " + s);
	}
	
	public void test(String s){
		System.out.println("enum s is: " + s);
	}
}
