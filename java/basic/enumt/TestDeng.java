package basic.enumt;

public class TestDeng {

	public static void main(String[] args) {
		Deng d = Deng.GREEN;
		System.out.println("d: " + d.toString());
		
		Deng [] all = Deng.getAll();
		for (int i = 0; i < all.length; i ++) {
			System.out.println(all[i]);
		}
		
		Deng1 [] d1 = Deng1.values();
		System.out.println(d1[0]);
		System.out.println(d1[2]);
	}

}
