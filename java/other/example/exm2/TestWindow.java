package day18.high;
import javax.swing.*;
import java.awt.event.*;

public class TestWindow {

	public TestWindow(){
		JFrame jf = new JFrame("TestWindow");
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.addWindowListener(new WindowListener(){

			public void windowActivated(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			public void windowClosed(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			public void windowClosing(WindowEvent e) {
				System.out.println("close");
				System.exit(1);  //ÍË³öjvm
			}

			public void windowDeactivated(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			public void windowDeiconified(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			public void windowIconified(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			public void windowOpened(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}
			
		});
	}
	public static void main(String[] args) {
		new TestWindow();
	}
}
