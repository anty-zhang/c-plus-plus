package day17.high;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.GridLayout;

public class Login {
	public static void main(String[] args) {
		JFrame jf = new JFrame("Login");
		jf.setLayout(new GridLayout(3,1));
		JPanel jp1 = new JPanel();
		JPanel jp2 = new JPanel();
		JPanel jp3 = new JPanel();
		JLabel jl1 = new JLabel("用户名：");
		JLabel jl2 = new JLabel("密    码：");
		JButton jb1 = new JButton("确定");
		JButton jb2 = new JButton("取消");
		JTextField jtf1 = new JTextField(10);
		JTextField jtf2 = new JTextField(10);
		jp1.add(jl1);
		jp1.add(jtf1);
		jp2.add(jl2);
		jp2.add(jtf2);
		jp3.add(jb1);
		jp3.add(jb2);
		
		jf.add(jp1);
		jf.add(jp2);
		jf.add(jp3);
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
