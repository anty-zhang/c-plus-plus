package day17.high;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.event.*;

public class Computer implements ActionListener {
	private boolean append = false;// 作为追加使用

	JTextField jtf = new JTextField(15);

	private String op1;

	private String op2;

	private String operator;

	public void actionPerformed(ActionEvent ae) {
		String mes = ae.getActionCommand();
		// String text = jtf.getText();
		// jtf.setText(mes);
		// if("BACK".equals(mes)){
		// jtf.setText(text.substring(0,text.length()-1));
		// }else if("CE".equals(mes)){
		// jtf.requestDefaultFocus();
		// }else if("C".equals(mes)){
		// jtf.requestDefaultFocus();
		// }else if("+".equals(mes)){
		//			
		// }
		// if(mes.matches("^\\d$")) //用正则
		if ("0123456789".indexOf(mes) != -1) {
			if (append) {
				String temp = jtf.getText();
				jtf.setText(temp + mes);
			} else {
				jtf.setText(mes);
				append = true;
			}
		} else if ("+-*/".indexOf(mes) != -1) {
			op1 = jtf.getText();
			operator = mes;
			append = false;
		} else if ("=".equals(mes)) {
			op2 = jtf.getText();
			double d1 = Double.parseDouble(op1);
			double d2 = Double.parseDouble(op2);
			if ("+".equals(operator)) {
				d1 = d1 + d2;
			} else if ("-".equals(operator)) {
				d1 = d1 - d2;
			} else if ("*".equals(operator)) {
				d1 = d1 * d2;
			} else {
				d1 = d1 / d2;
			}
			jtf.setText(d1 + "");
			append = false;
		} else if (".".equals(mes)){
			String temp = jtf.getText();
			if(temp.indexOf(".") == -1){
				jtf.setText(temp+".");
				append = true;
			}
		} else if (("+/-").equals(mes)){
			//1.＊ －1
			// 2. 追加－或去掉
			String temp = jtf.getText();
			if(temp.startsWith("-")){
				jtf.setText(temp.substring(1));
			}else{
				jtf.setText("-"+temp);
			}
			append = true;
		} else if (("BACK").equals(mes)){
			String temp = jtf.getText();
			if(temp.length()>0){  //判断长度
				jtf.setText(temp.substring(0,temp.length()-1));
			}
		} else {
			jtf.setText("");
			jtf.requestDefaultFocus();
			append = false;
		}
	}

	public Computer() {
		JFrame jf = new JFrame("Comput");
		 jtf.setEditable(false); //不能编辑
		jf.add(jtf, BorderLayout.NORTH);

		JPanel jp = new JPanel();
		jp.setLayout(new GridLayout(5, 4));

		String[] str = { "BACK", "CE", "C", "+", "7", "8", "9", "-", "4", "5",
				"6", "*", "1", "2", "3", "/", "0", "+/-", ".", "=" };
		// JButton[] jb = new JButton[20];
		JButton[] jb = new JButton[str.length];
		for (int i = 0; i < str.length; i++) {
			jb[i] = new JButton(str[i]);
			jb[i].addActionListener(this);
			jp.add(jb[i]);
		}
		jf.add(jp, BorderLayout.CENTER);

		jf.setResizable(false); // 不能拖拽

		jf.setSize(300, 200);
		jf.setLocation(300, 200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new Computer();
	}
}
