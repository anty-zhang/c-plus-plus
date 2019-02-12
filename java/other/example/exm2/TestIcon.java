package day18.high;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

import day17.high.Change;

public class TestIcon implements ActionListener{
	JTextField jtf1 = new JTextField(10);
	JTextField jtf2 = new JTextField(10);
	public void actionPerformed(ActionEvent ae){
		String temp = jtf1.getText();
		jtf1.setText(jtf2.getText());
		jtf2.setText(temp);
	}
	public TestIcon(){
		
		JFrame jf = new JFrame("change");
		jf.setLayout(new GridLayout(1,1));
		JPanel jp = new JPanel();
		Icon icon = new ImageIcon("/home/tarena01/3.jpg");
		JButton jb = new JButton(icon);
		jb.addActionListener( this);
		jtf1.addActionListener(this);
		jtf2.addActionListener(this);
		jp.add(jtf1);
		jp.add(jb);
		jp.add(jtf2);
		jf.add(jp);
		jf.setSize(500,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new Change();
	}

}
