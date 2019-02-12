package basic;

public class AnonymousInner {
	private int id;
	public static void main(String[] args) {
		Object obj1 = new Object();
		Object obj2 = new Object(){  //ÄäÃûÄÚ²¿Àà
			public void show(){
				System.out.println("show()");
			}
			@Override
			public String toString(){
				return "ok";
			}
			
			/*	@Override
			public boolean equals(Object obj){
				if(obj==null){
					return false;
				}else if(obj instanceof AnonymousInner){
					AnonymousInner ai = (AnonymousInner)obj;
					return ai.id==obj.
				}else{
					return false;
				}
			}
			*/
		};
		
		System.out.println(obj2);
		System.out.println(obj2.getClass());
		System.out.println(obj1);
	}
}
