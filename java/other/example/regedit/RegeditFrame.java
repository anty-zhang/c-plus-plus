package example.regedit;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class RegeditFrame implements ActionListener{
	JLabel jl1 = new JLabel("注册信息");
	JTextField jtf1 = new JTextField(10);
	JTextField jtf2 = new JTextField(10);
	JTextField jtf3 = new JTextField(10);
	
	public void actionPerformed(ActionEvent ae){
		String comm = ae.getActionCommand();
		if("注册".equals(comm)){
			String name = jtf1.getText();
			String password = jtf2.getText();
			if(password == null || !password.matches("^[a-zA-Z0-9_-]{6,8}$"))
				jl1.setText("密码6-8位，请重新输入");
			String email = jtf3.getText();
			Regedit regedit = new Regedit(name,password,email);
			try{
				String mes = regedit.regedit();
				jl1.setText(mes);
			}catch(Exception e){
				e.printStackTrace();
			}
		}else if("取消".equals(comm)){
			jtf1.setText("");
			jtf2.setText("");
			jtf3.setText("");
			jtf1.requestFocus(); //光标位置在首行
		}
	}
	
	public RegeditFrame(){
		JFrame jf = new JFrame("用户注册");
		jf.setLayout(new GridLayout(5,1));
		JPanel[] jp = new JPanel[5];
		for(int i=0;i<jp.length;i++){
			jp[i] = new JPanel();
		}
		
		JLabel jl2 = new JLabel("用户名：");
		JLabel jl3 = new JLabel("密  码：");
		JLabel jl4 = new JLabel("邮  件：");
		JButton jb1 = new JButton("注册");
		JButton jb2 = new JButton("取消");
		jb1.addActionListener(this);
		jb2.addActionListener(this);
		jp[0].add(jl1);
		jp[1].add(jl2);
		jp[1].add(jtf1);
		jp[2].add(jl3);
		jp[2].add(jtf2);
		jp[3].add(jl4);
		jp[3].add(jtf3);
		jp[4].add(jb1);
		jp[4].add(jb2);
		for(int i = 0;i<jp.length;i++){
			jf.add(jp[i]);
		}
		
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new RegeditFrame();
	}
}
