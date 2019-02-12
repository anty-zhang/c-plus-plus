package socket.tcp.exp1.version3;

import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;

public class TestServer {
	public static void socketServer() throws Exception {
		ServerSocket ss = new ServerSocket(8888);
		// create one socket
		System.out.println("create one socket begin");
		while (true) {
			Socket s = ss.accept();
			new SocketServerThread(s).start();
			System.out.println("create one socket end");
		}
//		ss.close();
	}
	public static void main(String[] args) throws Exception {
		TestServer.socketServer();
	}
}
