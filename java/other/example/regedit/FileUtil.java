package example.regedit;
import java.util.List;
import java.util.ArrayList;
import java.io.*;

public class FileUtil {
	public static List<User> getUser() throws IOException{
		List<User> list = new ArrayList<User>();
		File file = new File("./src/example/regedit/regedit.xml");
		System.out.println(file.getPath());
		if(!file.exists()) file.createNewFile(); //如果文件不存在，则创建
		System.out.println(file.exists());
		FileInputStream fis = new FileInputStream("./src/example/regedit/regedit.xml");
		InputStreamReader isr = new InputStreamReader(fis); //一行一行的读
		BufferedReader br = new BufferedReader(isr);
		while(true){
			String temp = br.readLine();
			if(temp == null) break;     //文件读到空，循环结束
			String[] mes = temp.split(",");
			if(mes.length!=3){          //数组不为3，则为不合法信息
				continue;
			}
			User user = new User(mes[0],mes[1],mes[2]);
			list.add(user);
		}
		br.close(); //关闭包装流
		return list;
	}
	
	public static void setUser(String mes) throws IOException{
		FileOutputStream fos = new FileOutputStream("./src/example/regedit/regedit.xml",true);//true
		PrintStream ps = new PrintStream(fos);   //一行一行的写
		ps.println(mes);
		ps.close();    //关闭包装流
	}
}
