package io;

import java.io.File;
import java.io.FilenameFilter;


/*
 * 文件过滤器
 */
public class TestFileFilter {

	public static void main(String[] args) {
		File file = new File("./");
		String [] mes = file.list(new FilenameFilter() {
			public boolean accept(File f, String s) {
				System.out.println("accept: " + s);
				return s.endsWith(".java") || s.endsWith(".pdf");
			}

		});
		
		for (String s: mes) {
			System.out.println(s);
		}

	}

}
