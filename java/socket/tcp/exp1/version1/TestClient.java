package socket.tcp.exp1.version1;

import java.net.Socket;
import java.io.*;

/*
 * socket 应用1
 * 从客户端TestClient输入内容发送到服务器TestServer
 * TestServer服务器接受内容，经过处理后发给客户端TestClient
 * TestClient客户端接受服务器的内容
 */
public class TestClient {
	
	public static void socketClient() throws Exception {
		Socket so = new Socket("127.0.0.1", 8888);
		// input string
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		String msg = br.readLine();
		
		// output to socket
		DataOutputStream dos = new DataOutputStream(so.getOutputStream());
		dos.writeUTF(msg);	// sent the msg to TestServer
		
		// fetch msg from socket which is TestServer
		DataInputStream dis = new DataInputStream(so.getInputStream());
		System.out.println(dis.readUTF());
		
		// close streams
		br.close();
		dos.close();
		dis.close();
		so.close();
	}

	public static void main(String[] args) throws Exception {
		TestClient.socketClient();
	}

}
