package day19.high;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ProgressBarH extends Thread implements ActionListener{
	JProgressBar jpb = new JProgressBar(0,200);
	public void actionPerformed(ActionEvent ae){
		this.start();
	}
	@Override
	public void run(){
		for(int i=0;i<=200;i++){
			jpb.setValue(i);
			jpb.setBounds(30, 30, 200, 20);
//			jpb.setBackground(Color.blue);
			jpb.setBorderPainted(true);
//			jpb.setForeground(Color.green);
			jpb.setStringPainted(true); //显示进度条上的数字进度
			try{
				Thread.sleep(100);
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	
	public ProgressBarH(){
		JFrame jf = new JFrame("ProgressBarH");
		jf.setLayout(new GridLayout(2,1));
		
		//jpb.addChangeListener();
		JPanel jp1 = new JPanel();
		jp1.add(jpb);
		jf.add(jp1);
		
		JButton jb = new JButton("Start");
		jb.addActionListener(this);
		JPanel jp2 = new JPanel();
		jp2.add(jb);
		jf.add(jp2);
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new ProgressBarH();
	}

}