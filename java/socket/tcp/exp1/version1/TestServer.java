package socket.tcp.exp1.version1;

import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;

public class TestServer {
	public static void socketServer() throws Exception {
		ServerSocket ss = new ServerSocket(8888);
		// create one socket
		System.out.println("create one socket begin");
		Socket s = ss.accept();
		System.out.println("create one socket end");
		
		// fetch msg from client socket
		DataInputStream dis = new DataInputStream(s.getInputStream());
		String msg = dis.readUTF();
		
		// server msg send to client socket
		DataOutputStream dos = new DataOutputStream(s.getOutputStream());
		dos.writeUTF("server: " + msg);
		
		// close the streams
		ss.close();
		s.close();
		dis.close();
		dos.close();
	}
	public static void main(String[] args) throws Exception {
		TestServer.socketServer();
	}
}
