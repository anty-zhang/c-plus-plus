package day18.high;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TestAdapter {
	public  TestAdapter(){
		JFrame jf = new JFrame("TestAdapter");
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.addWindowListener(new WindowAdapter(){   //用Adapter来实现Window监听
			public void windowClosing(WindowEvent we){
				System.out.println("close ok");
				System.exit(1);
			}
		});
		
	}
	
	public static void main(String[] args) {
		new TestAdapter();
	}

}
