package day17.high;
import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.BorderLayout;

public class TestBoerLayout {
	public static void main(String[] args) {
		JFrame jf = new JFrame("TestBorderLayout");
		String[] pos = {BorderLayout.EAST,BorderLayout.SOUTH, //字符串一一对应
				BorderLayout.WEST,BorderLayout.NORTH,BorderLayout.CENTER};
		String[] s = {"EAST","SOUTH","WEST","NORTH","CENTER"};
		JButton[] jb = new JButton[s.length];
		for(int i=0;i<jb.length;i++){
			jb[i] = new JButton(s[i]);
			jf.add(jb[i],pos[i]);
		}
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

}
