package socket.tcp.exp1.version2;

import java.net.Socket;
import java.io.*;

/*
 * socket 应用2
 * 在version1的基础上
 * 服务器端不间断接受客户端的请求(服务器只能接受一个客户端请求)
 * 客户端循环直至输入bye结束和服务端的通信
 */
public class TestClient {
	
	public static void socketClient() throws Exception {
		Socket so = new Socket("127.0.0.1", 8888);
		
		// input string
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
					
		// output to socket
		DataOutputStream dos = new DataOutputStream(so.getOutputStream());
		// fetch msg from socket which is TestServer
		DataInputStream dis = new DataInputStream(so.getInputStream());
		while(true) {
			String msg = br.readLine();
			if ("bye".equals(msg)) break;
			dos.writeUTF(msg);	// sent the msg to TestServer
			System.out.println(dis.readUTF());
		}
		
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
