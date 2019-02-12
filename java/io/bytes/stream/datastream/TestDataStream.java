package io.bytes.stream.datastream;
import java.io.*;

public class TestDataStream {

	public static void main(String[] args) throws Exception {
		DataInputStream dis = new DataInputStream(System.in);
		String msg = dis.readUTF();
		
		FileOutputStream fos = new FileOutputStream("./src/io/bytes/stream/datastream/out.txt");
		DataOutputStream dos = new DataOutputStream(fos);
		dos.writeUTF(msg);
		
		dis = new DataInputStream(new FileInputStream("./src/io/bytes/stream/datastream/out.txt"));
		String readline = dis.readUTF();
		System.out.println("readLine:" + readline);
		dis.close();
		dos.close();
	}

}
