package io.randaccessfile;

import java.io.RandomAccessFile;

/*
 * RandomAccessFile 应用
 */
public class TestRandomAccessFile {

	private static RandomAccessFile rafr;
	private static RandomAccessFile rafw;

	public static void main(String[] args) {
		try {
			rafr = new RandomAccessFile("./src/io/randaccessfile/read.txt", "r");
			rafw = new RandomAccessFile("./src/io/randaccessfile/write.txt", "rw");
			byte [] b = new byte[(int)rafr.length()];
			rafr.read(b);
			rafw.seek(rafw.length());
			rafw.write(b);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
