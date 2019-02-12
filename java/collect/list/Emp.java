package collect.list;

/*	1. Override
 * 	2. 重写equals，hashCode，toString方法
 */
public class Emp {
	private String name;
	private String id;
	private double sal;
	
	// 空构造函数
	public Emp() {
		super();
	}
	
	// 带参数构造函数
	public Emp(String name, String id, double sal) {
		super();
//		this.name = name;
//		this.id = id;
//		this.sal = sal;
		this.setName(name);
		this.setId(id);
		this.setSal(sal);
	}
	
	//重写equals方法
	// Override 作用： 重写父类中的方法；编译时做检查
	@Override
	public boolean equals(Object obj) {
		//  第一步：判断两个对象的地址是否相等
		//	第二步：如果参数为null，则直接返回false
		//	第三步：判断两个对象是不是同一个类型，如果不是返回false
		//	第四步：将待比较对象强制转成指定类型，然后自定义比较规则
		if (this == obj) {
			return true;
		} else if(null == obj) {
			return false;
		} else if (obj instanceof Emp) {
			Emp e = (Emp)obj;
			return e.id.equals(this.id);
		}else {
			return false;
		}
		
	}
	//重写hashCode
	@Override
	public int hashCode() {
		int type = 29;
		int code = type * 41 + getId().hashCode();
		return code;
	}
	//重写toString
	@Override
	public String toString() {
		return "name: " + this.getName() 
		+ "; id: " + this.getId() 
		+ "; sal:" + this.getSal();
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public double getSal() {
		return sal;
	}
	public void setSal(double sal) {
		this.sal = sal;
	}
	
	
}
