package designmode.state;

public class Go {
	private IState state;
	public Go(IState state) {
		this.state = state;
	}
	
	public void go() {
		state.go();
	}
	
	public static void main(String[] args) {
		Go g = new Go(new YelloState());
		g.go();
	}
}
