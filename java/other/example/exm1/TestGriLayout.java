package day17.high;
import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.GridLayout;

public class TestGriLayout {
	public static void main(String[] args) {
		JFrame jf = new JFrame("TestGridLayout");
		jf.setLayout(new GridLayout(5,4));
		JButton[] jb = new JButton[20];
		for(int i=0;i<jb.length;i++){
			jb[i] = new JButton("Button"+i);
			jf.add(jb[i]);
		}
		
		jf.setSize(400,300);
		jf.setLocation(400,300);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

}
