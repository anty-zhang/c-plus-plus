package day16;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Regedit {
	public static void regedit() {
		Scanner sc = new Scanner(System.in);
		System.out.println("input name,password,email;");
		String name = sc.next();
		String password = sc.next();
		String email = sc.next();

		String temp = Regedit.getFileInput(); //
		if (temp.endsWith(";")) {
			temp = temp.substring(0, temp.length() - 1);
		}

		if (temp == null || "".equals(temp)) { //
			User user = new User(name, password, email);
			Regedit.setFileOutput(user);
		} else {
			List<User> list = new ArrayList<User>(); //
			String[] s = temp.split(";");
			for (String ss : s) {
				String[] u = ss.split(",");
				User user = new User(u[0], u[1], u[2]); //
				list.add(user); //
			}

			boolean flag = false;
			for (User u : list) {
				if (u.getName().equals(name)) { //
					flag = true;
					System.out.println("用户名有重复");
					break;
				}
			}

			if (!flag) {
				User user = new User(name, password, email);
				Regedit.setFileOutput(user);
				System.out.println("regedit sueccess!");
			}
		}
	}

	public static String getFileInput() {
		String temp = "";
		try {
			FileInputStream fis = new FileInputStream(
					"/home/tarena01/workspace/corejava/day16/regedit.txt");
			byte[] b = new byte[1024];
			while (true) {
				int num = fis.read(b);
				if (num == -1) {
					break;
				}
				temp = temp + new String(b, 0, num);
			}
			fis.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return temp;
	}

	public static void setFileOutput(User user) {
		try {
			FileOutputStream fos = new FileOutputStream(
					"/home/tarena01/workspace/corejava/day16/regedit.txt", true);
			fos.write(user.toString().getBytes());
			fos.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws Exception {
		Regedit.regedit();
	}
}

/*
 * 模拟用户注册的过程 要求：用户注册信息（用户名／密码／email）通过 Scanner录入，检测一下用户名是否存在，不存在，把用户写入文件
 * （用FileInputStream读入一个文件，得到所有用户的信息List（User），循环比较用户名） 注意：先建立文件，否则会出现异常
 * （写入时，设定拆分条件，追加方式）
 */