package socket.udp;

import java.net.InetAddress;

public class TestInetAddress {

	public static void main(String[] args) throws Exception {
		InetAddress ia = InetAddress.getLocalHost();
		System.out.println(ia);		// 192.168.1.101
		byte [] b = ia.getAddress();
		for(byte bb: b) {
			System.out.println(bb);
		}
		
		byte[] b1 = {-64, -88, 1, 101};
		InetAddress ia1 = InetAddress.getByAddress(b1);
		System.out.println(ia1);
	}

}
