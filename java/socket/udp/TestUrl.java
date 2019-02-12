package socket.udp;

import java.io.*;
import java.net.URL;
import java.net.URLConnection;
/*
 * URL, URLConnection 使用
 */

public class TestUrl {
	public static void testURL() throws Exception {
		URL url = new URL("https://www.baidu.com/");
		URLConnection urlc = url.openConnection();		// open connection
		InputStream is = urlc.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);
		
		while(true) {
			String msg = br.readLine();
			if (null == msg) break;
			System.out.println(msg);
		}
		
		br.close();
		
	}
	
	public static void main(String[] args) throws Exception {
		TestUrl.testURL();
	}
}
