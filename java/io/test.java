package io;

import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


/*输入／输出流： 字节流和字符流
 * 1.File类
 * 	创建目录和文件；
 * 	不能访问文件中的内容；
 * 	主要方法：
 * 		File fn = new File("test.txt");
 * 		fn.createNewFile();
 * 		
 * 		File fd = new File("p/q/s);
 * 		fd.mkdir();
 * 		fd.mkdirs();
 * 		fd.list();
 * 		fd.isDirectory();
 * 		fd.isFile();
 * 		fd.delete();
 * 		fd.deleteOnExit();
 * 
 * 2.字节流
 * 	（1）继承关系图
 * 	输入流类图
 * 		InputStream
 * 			FileInputStream， PipeInputStream（节点流）
 * 			FilterInputStream	（过滤流）
 * 				DataInputStream		（读写字符）
 * 				BufferedInputStream	（读写字节）
 * 			ByteArrayInputStream
 * 			SequenceInputStream
 * 			OjbectInputStream
 * 	输出流类图
 * 		OutputStream
 * 			FileOutputStream，PipeOutputSteam
 * 			FilterOutputStream
 * 				DataOutputStream
 * 				BufferedOutputStream
 * 			ByteArrayOutputStream
 * 			SequenceOutputStream
 * 			ObjectOutputStream
 * 
 * 	节点流：真正的和一个文件创建的连接的流，具有基本的字节读写能力
 * 	过滤流：主要给节点流增加一些功能
 * 
 *		
 * 3.字符流
 * 	保证编解码统一，防止出现乱码；
 * 	（1）输入流
 * 		Reader
 * 			BufferedReader
 * 			PipedReader
 * 			CharArrayReader
 * 		FileReader					（节点流）
 * 			InputStreamReader		（字节流到字符流的桥梁）
 * 
 * 	（2）输出流
 * 		Writer
 * 			BufferedWriter
 * 			PipedWriter
 * 			PrintWriter
 * 			CharArrayWriter
 * 		FileWriter
 * 			OutputStreamWriter
 * 
 */

public class test {
	public static void main(String[] args)
	{
//		test.ByteStreamCopyTest();
		test.CharacterStreamCopyTest();
		
	}
	
	public static void CharacterStreamCopyTest(){
		System.out.println("character stream copy test bengin");
		try {
			FileInputStream fis = new FileInputStream("/Users/guoqiangzhang/input.txt");
			BufferedReader br = new BufferedReader(new InputStreamReader(fis));
			
			
			FileOutputStream fos = new FileOutputStream("/Users/guoqiangzhang/output1.txt");
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
			
			String s = br.readLine();
			System.out.println("out while: " + s);
			while (s != null && !"".equals(s)) {
				System.out.println("enter while: " + s);
				bw.write(s+"\n");
				s = br.readLine();
			}
			bw.flush();
			br.close();
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("character stream copy test end");
	}
	
	public static void ByteStreamCopyTest() {
		System.out.println("byte stream copy test begin");
		try {
			FileInputStream fis = new FileInputStream("/Users/guoqiangzhang/input.txt");
			BufferedInputStream bis = new BufferedInputStream(fis);
			
			
			FileOutputStream fos = new FileOutputStream("/Users/guoqiangzhang/output.txt");
			BufferedOutputStream bos = new BufferedOutputStream(fos);
			
			byte [] b = new byte[1024];	// 作为缓冲区，1k
			int len = -1;				// 保存实际都到的字节数
			while((len = bis.read(b)) != -1){
				bos.write(b, 0, len);		// 写到Socket中
				bos.flush();			// 清空缓冲区
			}
			
			bis.close();
			bos.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			
		}
		System.out.println("byte stream copy test end");
	}
}
