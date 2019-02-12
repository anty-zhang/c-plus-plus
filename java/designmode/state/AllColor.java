package designmode.state;

public class AllColor {
	public enum GoColor{RED, GREEN, YELLOW};
	private GoColor gc;
	
	public void go() {
		if (gc.equals(GoColor.RED)) {
			System.out.println("enum color red");
		} else if (gc.equals(GoColor.GREEN)) {
			//
		} else {
			
		}
	}
	
	public GoColor getGc() {
		return gc;
	}
	
	public void setGc(GoColor gc) {
		this.gc = gc;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AllColor a = new AllColor();
		System.out.println(a.getGc());
	}

}
