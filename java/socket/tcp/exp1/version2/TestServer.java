package socket.tcp.exp1.version2;

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
			System.out.println("create one socket end");
			
			DataInputStream dis = new DataInputStream(s.getInputStream());
			DataOutputStream dos = new DataOutputStream(s.getOutputStream());
			
			while(true) {
				String msg = dis.readUTF();		// fetch msg from client socket
				if ("bye".equals(msg))  break;
				dos.writeUTF("server: " + msg);  // server msg send to client socket
			}
			// close the streams
			s.close();
			dis.close();
			dos.close();
		}
//		ss.close();
	}
	public static void main(String[] args) throws Exception {
		TestServer.socketServer();
	}
}
