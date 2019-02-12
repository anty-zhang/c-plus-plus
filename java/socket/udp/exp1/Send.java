package socket.udp.exp1;

import java.io.*;
import java.net.InetAddress;
import java.net.DatagramSocket;
import java.net.DatagramPacket;

public class Send {
	
	public static void testSend() throws Exception {
		DatagramSocket ds = new DatagramSocket();
		InputStream is = System.in;
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);
		while(true) {
			String msg = br.readLine();
			if ("bye".equals(msg)) {
				System.out.println("send exit");
				break;
			}
			byte[] b = msg.getBytes();	// bytes
			
			// construct Datagram packet
			DatagramPacket dp = new DatagramPacket(b, b.length, InetAddress.getLocalHost(), 8888);
			ds.send(dp);
		}
		ds.close();
	}

	public static void main(String[] args) throws Exception {
		Send.testSend();
	}
}
