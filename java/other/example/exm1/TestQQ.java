package day17.high;
/*
1.确定组件
2.分析布局管理器
3.选择容器
4.为容器设置布局管理，把组件加入对应的容器
 */
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import javax.swing.JPanel;
import java.awt.FlowLayout;
import java.awt.BorderLayout;

public class TestQQ {
	public static void main(String[] args) {
		JFrame jf = new JFrame("TestQQ");
		JTextField jtf = new JTextField(20);
		JButton jb = new JButton("发送");
		JPanel jp = new JPanel();
		
		jp.add(jtf);
		jp.add(jb);
		jp.setLayout(new FlowLayout());
		JTextArea jta = new JTextArea(10,30);
		
		jta.setEditable(false);
		
		jf.add(jta,BorderLayout.CENTER);
		jf.add(jp,BorderLayout.SOUTH);
		
		jf.setSize(500,400);
		jf.setLocation(500,400);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

}
