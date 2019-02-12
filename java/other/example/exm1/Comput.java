package day17.high;
/*
写计算器的界面，一个文本框，20个按钮
BACKSPACE，CE，C，E，
7，8，9，－
4，5，6，＊
1，2，3，／
0，＋／－，。，＝
 */
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.GridLayout;

public class Comput {
	public static void main(String[] args) {
		JFrame jf = new JFrame("Comput");
		JTextField jtf = new JTextField(15);
		jtf.setEditable(false); //不能编辑
		jf.add(jtf,BorderLayout.NORTH);
		
		JPanel jp = new JPanel();
		jp.setLayout(new GridLayout(5,4));
		
		String[] str = {"BACK","CE","C","+",	"7","8","9","-", "4","5","6","*","1","2","3","/", "0","+/-",".","="};
		//JButton[] jb = new JButton[20];
		JButton[] jb = new JButton[str.length];
		for(int i=0;i<str.length;i++){
			jb[i] = new JButton(str[i]);
			jp.add(jb[i]);
		}
		jf.add(jp,BorderLayout.CENTER);
		
		jf.setResizable(false);   //不能拖拽
		
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

}
