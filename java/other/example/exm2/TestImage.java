package day18.high;

import java.awt.FlowLayout;

import javax.swing.*;

public class TestImage {

	public TestImage(){
		Icon icon1 =new ImageIcon("/home/tarena01/2.jpg");
//		Icon icon2 =new ImageIcon("/home/tarena01/4.jpg");
//		Icon icon3 =new ImageIcon("/home/tarena01/2.jpg");
//		Icon icon4 =new ImageIcon("/home/tarena01/1.jpg");
		JFrame jf = new JFrame();
//		JButton jb1 = new JButton(icon1);
//		JButton jb2 = new JButton(icon2);
//		JButton jb3 = new JButton(icon3);
//		JButton jb4 = new JButton(icon4);
		
		JButton jb1 = new JButton(icon1);
		JButton jb2 = new JButton("2");
		JButton jb3 = new JButton("3");
		JButton jb4 = new JButton("4");
		jb1.setActionCommand("change");

		
		JPanel jp = new JPanel();
		jp.setLayout(new FlowLayout());
		jp.add(jb1);
		jp.add(jb2);
		jp.add(jb4);
		jp.add(jb3);
		
		jf.add(jp);
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new TestImage();
	}

}
