package socket.udp.exp1;

import java.net.DatagramSocket;
import java.net.DatagramPacket;

public class Receive {
	public static void receive() throws Exception {
		DatagramSocket ds = new DatagramSocket(8888);		// socket
		
		byte [] b = new byte[2048];
		DatagramPacket dp = new DatagramPacket(b, b.length);
		while(true) {
			System.out.println("receive one message start.");
			ds.receive(dp);
			System.out.println("receive: " + new String(b, 0, dp.getLength()));
			System.out.println("receive one message end.");
		}
//		ds.close();
	}

	public static void main(String[] args) throws Exception {
		Receive.receive();
	}
}
