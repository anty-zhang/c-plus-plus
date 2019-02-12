package socket.chatroom;

import java.net.*;
import java.io.*;

public class Client_socket extends Thread {
	private DataInputStream in;

	private DataOutputStream out;

	private String clientname;

	private History history_info;

	public Client_socket(Socket tt, History history_info) {
		this.history_info = history_info;
		// 搭建与server_socket的联系
		try {
			InputStream is = tt.getInputStream();
			in = new DataInputStream(is);

			OutputStream ops = tt.getOutputStream();
			out = new DataOutputStream(ops);

		} catch (Exception e) {
			System.out.println(1);
			System.out.println(e);
		}

	}

	public void run() {
		String ww = "";
		try {
			while (true) {
				ww = in.readUTF();
				// 客户机注册
				if (ww.equals("<1.1>")) {
					clientname = in.readUTF();
					history_info.setWord("server: 欢迎" + clientname + "加入聊天室");
				}
				// client 要求得到所有的信息
				else if (ww.equals("<2.1>")) {
					out.writeUTF(history_info.getWord());
				}
				// client要发言
				else if (ww.equals("<2.2>")) {
					history_info.setWord(clientname + "说：" + in.readUTF());
				}
				// client离开
				else if (ww.equals("<3.2>")) {
					history_info.setWord(clientname + "离开了聊天室。");
				}
			}
		} catch (Exception e) {
			System.out.println(2);
			System.out.println(e);
		}
	}

};