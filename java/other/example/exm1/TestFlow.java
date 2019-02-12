package day17.high;
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextField;

import java.awt.FlowLayout;

public class TestFlow {
	public static void main(String[] args){
		JFrame jf = new JFrame("TestFlow");
		jf.setLayout(new FlowLayout());
		jf.setSize(300,200);
		jf.setLocation(300,200);
		
		JTextField jtf = new JTextField(10);
		jf.add(jtf);
		JButton[] jb = new JButton[10];
		for(int i=0;i<jb.length;i++){
			jb[i] = new JButton("Buuton"+i);
			jf.add(jb[i]);
		}
		
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
