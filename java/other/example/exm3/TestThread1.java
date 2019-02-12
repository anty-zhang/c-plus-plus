package day19.high;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TestThread1 extends Thread implements ActionListener {
	JLabel jl = new JLabel("20");
	private int time = 20;

	public void actionPerformed(ActionEvent ae) {
		String mes = ae.getActionCommand();
		if ("start".equals(mes)) {
			try{
				this.start();  //thisÓÃ·¨
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}

	@Override
	public void run() {
		for (; time > 0; time--) {
			jl.setText(time + "");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public TestThread1() {
		JFrame jf = new JFrame("TestThread1");
		jf.setLayout(new FlowLayout());
		jf.add(jl);
		JButton jb = new JButton("start");
		jb.addActionListener(this);
		jf.add(jb);
		JButton jb1 = new JButton("stop");
		jb1.addActionListener(this);
		jf.add(jb1);

		jf.setSize(300, 200);
		jf.setLocation(300, 200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new TestThread1();
	}
}
