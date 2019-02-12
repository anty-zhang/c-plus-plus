package example.regedit;

public class User {
	private String name;
	private String password;
	private String email;
	public User(){}
	public User(String name,String password,String email){
		this.setName(name);
		this.setPassword(password);
		this.setEmail(email);
	}
	@Override 
	public boolean equals(Object obj){
		if(obj == null) return false;
		if(obj == this) return true;
		if(obj.getClass() == this.getClass()){
			final User user = (User)obj;
			return user.getName().equals(name);
		}else{
			return false;
		}
	}
	@Override
	public int hashCode(){
		int type = 29;
		int code = type*41 + name.hashCode();
		return code;
	}
	@Override
	public String toString(){
		return getName()+","+getPassword()+","+getEmail();
	}
	
	public void setName(String name){
		this.name = name;
	}
	public String getName(){
		return name;
	}
	public void setPassword(String password){
		this.password = password;
	}
	public String getPassword(){
		return password;
	}
	public void setEmail(String email){
		this.email = email;
	}
	public String getEmail(){
		return email;
	}
}
