package io.bytes.stream.copyfile;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class TestCopyFile {
	public static String inputFile() {
		FileInputStream fis = null;
		String temp = "";
		try {
			fis = new FileInputStream("./src/io/bytes/stream/copyfile/io.txt");
			byte [] b = new byte[16];
			while(true) {
				int i = fis.read(b);		// read
				if (-1 == i) {
					break;
				}
				temp += new String(b, 0, i);		// byte to String
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				fis.close();				// close
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return temp;
	}
	
	public static void outputFile() {
		/*
		 * 将输入文件内容从字节转为String
		 * 再将String转为字节写入文件
		 */
		String msg = TestCopyFile.inputFile();
		FileOutputStream fos = null;
		try {
			fos = new FileOutputStream("./src/io/bytes/stream/copyfile/out.txt", true); // true???
			fos.write(msg.getBytes());		// string to bytes
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				fos.close();						// close
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void copyFile() {
		/*
		 * 直接读字节流，直接写字节流
		 */
		FileInputStream fis = null;
		FileOutputStream fos = null;
		try {
			fis = new FileInputStream("./src/io/bytes/stream/copyfile/io.txt");
			fos = new FileOutputStream("./src/io/bytes/stream/copyfile/out1.txt", true);
			
			byte [] b = new byte[8];
			while (true) {
				int i = fis.read(b);
				if (-1 == i) {
					break;
				}
				fos.write(b, 0, i);
			}
			fis.close();
			fos.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}

	public static void main(String[] args) {
//		TestCopyFile.outputFile();
		TestCopyFile.copyFile();
	}
}
