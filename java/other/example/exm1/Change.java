package day17.high;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Change implements ActionListener{
	JTextField jtf1 = new JTextField(10);
	JTextField jtf2 = new JTextField(10);
	public void actionPerformed(ActionEvent ae){
		String temp = jtf1.getText();
		jtf1.setText(jtf2.getText());
		jtf2.setText(temp);
	}
	public Change(){
		JFrame jf = new JFrame("change");
		jf.setLayout(new GridLayout(1,1));
		JPanel jp = new JPanel();
		
		JButton jb = new JButton("change");
		jb.addActionListener(this);
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
