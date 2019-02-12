package day17.high;
import java.awt.event.*;
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.FlowLayout;

public class TestNumber implements ActionListener{//static   //1实现接口
	JLabel jl = new JLabel("welcome !!");                      //提升变量
	private int num = 0;
	public void actionPerformed(ActionEvent ae){               //重写方法
		String mes = ae.getActionCommand();
		if("+".equals(mes))
			num++;
		else if("-".equals(mes))
			num--;
		jl.setText("you click "+num+" times!");
	}
	
	public TestNumber(){                                     //移植代码
		JFrame jf = new JFrame();
		jf.setLayout(new FlowLayout());
		jf.add(jl);
		JButton jb1 = new JButton("+");
		jb1.addActionListener(this);    //this                 //注册监听
		jf.add(jb1);
		JButton jb2 = new JButton("-");
		jb2.addActionListener(this);
		jf.add(jb2);
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new TestNumber();
	}

}
