package io.bytes.stream.printstream;

import java.io.*;

public class TestPrintStream {

	public static void main(String[] args) throws Exception {
		// input
		InputStream is = System.in;
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);
		
		// output
		FileOutputStream fos = new FileOutputStream("./src/io/bytes/stream/printstream/out.txt", true);
		PrintStream ps = new PrintStream(fos);
		for (int i = 0;; i++) {
			String temp = br.readLine();
			if ("bye".equals(temp)) {
				break;
			}
			ps.println(i + "." + temp);		// write file
		}
		
		ps.close();
		br.close();
	}

}
