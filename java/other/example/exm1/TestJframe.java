package day17.high;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JButton;

public class TestJframe {
	public static void main(String[] args) {
		JFrame jf = new JFrame("TestJframe");
		JButton jb = new JButton(new ImageIcon("/home/tarena01/3.jpg","ok"));
		jf.setSize(300,200);//设置大小
		jf.setLocation(300, 200);//设置显示位置
		jf.add(jb);    //把按钮放入窗口
		jf.setVisible(true);//设置可见
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//关闭退出
	}

}
