package socket.tcp.exp1.version3;

import java.net.Socket;
import java.io.DataInputStream;
import java.io.DataOutputStream;

public class SocketServerThread extends Thread {
	private Socket so = null;
	public SocketServerThread(Socket so) {
		this.so = so;
	}
	
	@Override
	public void run() {
		try {
			DataInputStream dis = new DataInputStream(so.getInputStream());
			DataOutputStream dos = new DataOutputStream(so.getOutputStream());
		
			while (true) {
				String msg = dis.readUTF();
				if ("bye".equals(msg)) {
					break;
				}
				dos.writeUTF("server:" + msg);
			}
			so.close();
			dis.close();
			dos.close();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
