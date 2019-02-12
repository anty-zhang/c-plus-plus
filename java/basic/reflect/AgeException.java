package basic.reflect;

/*
 * 自定义异常
 */
public class AgeException extends Exception {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	public AgeException() {
		this("Age too large");
	}
	
	public AgeException(String msg) {
		super(msg);
	}

}
