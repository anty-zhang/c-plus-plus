package day19.high;
//子类可以对父类作修改
public class MiceAdapter extends Mice{
	private Meat meat;
	public MiceAdapter(Meat meat){
		this.meat=meat;
	}
	@Override
	public void sellMice(){
		meat.sellMeat();
	}
	
	public static void main(String[] args) {
		Mice m = new Mice();
		m.sellMice();
		Meat mt = new Meat();
		Mice ma =new MiceAdapter(mt);//强制性
		ma.sellMice();
	}
}
