package io.c.bufferedreader;

import java.io.*;

/*
 * 
 * bufferedreader 使用
 */

public class TestBufferedReader {

	public static void main(String[] args) throws Exception {
		FileInputStream fis = new FileInputStream("./src/io/bytes/stream/printstream/out.txt");
		InputStreamReader isr = new InputStreamReader(fis);
		BufferedReader br = new BufferedReader(isr);
		
		int i = 1;
		while(true) {
			String temp = br.readLine();
			if (null == temp) {
				break;
			}
			System.out.println("i: " + i + ", " + temp);
			i++;
		}
	}

}
