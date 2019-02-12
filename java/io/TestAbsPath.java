package io;

import java.io.File;

public class TestAbsPath {

	public static void main(String[] args) {
		File file = new File("./");
		System.out.println(file.exists());
		
		System.out.println(file.getAbsolutePath());

	}

}
