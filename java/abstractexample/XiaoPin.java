package abstractexample;

// not private static final
public abstract class XiaoPin {
	// function: not private static final
	abstract void jiaoliu(); 
	abstract void xushi(); 
	abstract void gaoxiao(); 
	abstract void shanqing(); 
	public final void act(){
		jiaoliu();
		xushi();
		gaoxiao();
		shanqing();
	}
}
