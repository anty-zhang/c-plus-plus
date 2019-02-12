package socket.chatroom;

import java.net.*;
import java.util.*;
import java.io.*;

public class Server_socket extends Thread {
	private ServerSocket scoket;

	private History history_info = new History();

	private Vector clientnum = new Vector();

	public void run() {
		try {
			scoket = new ServerSocket(2222);
			while (true) {
				Socket sc = scoket.accept();
				clientnum.addElement(sc);
				System.out.println(sc);
				Client_socket ddd = new Client_socket(sc, history_info);
				ddd.start();
			}
		} catch (Exception e) {
			System.out.println(3);
			System.out.println(e);
		}
	}

	public void stop_server() {
		try {
			scoket.close();
			Enumeration sc = clientnum.elements();
			while (sc.hasMoreElements()) {
				Socket sc1 = (Socket) sc.nextElement();
				sc1.close();
				System.out.println("some client is rejected");
			}
			clientnum.clear();
		} catch (Exception e) {
			System.out.println(5);
			System.out.println(e);
		}

	}
}