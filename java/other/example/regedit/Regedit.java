package example.regedit;
import java.io.IOException;
import java.util.List;

public class Regedit {
	private String name;
	private String password;
	private String email;
	public Regedit(String name,String password,String email){
		this.name = name;
		this.password = password;
		this.email = email;
	}
	public String regedit() throws IOException{
		String mes =null;
			List<User> list = FileUtil.getUser();
			boolean flag = true;
			for(User user:list){
				if(name.equals(user.getName())){
					flag = false;
					mes = "用户名重复！";
					break;
				}
			}
			
			if(flag){
				FileUtil.setUser(name+","+password+","+email);
				mes = "注册成功";
			}
			return mes;
	}
}
