package day18.high;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ImageShow implements ActionListener{
	CardLayout cl = new CardLayout();
	JPanel jp1= new JPanel();
	
	public void actionPerformed(ActionEvent ae){
		String mes = ae.getActionCommand();
		if("first".equals(mes)){
			cl.first(jp1);         //*******************************
		}else if("last".equals(mes)){
			cl.last(jp1);
		}else if("next".equals(mes)){
			cl.next(jp1);
		}else{
			cl.previous(jp1);
		}
	}
	
	public ImageShow(){
		JFrame jf = new JFrame("ImageShow");
		String[] lab = {"1.jpg","2.jpg","3.jpg","4.jpg"};
		
		
		jp1.setLayout(cl);
		for(int i=0;i<lab.length;i++){
			Icon icon = new ImageIcon("/home/tarena01/"+lab[i]);
			JLabel jl = new JLabel(icon);  
			jp1.add(jl,lab[i]);                   //*****************
		}
		jf.add(jp1,BorderLayout.CENTER);
		
		String[] blab = {"first","last","next","previous"};
		JPanel jp2 = new JPanel();
		for(int i=0;i<blab.length;i++){
			JButton jb = new JButton(blab[i]);
			jp2.add(jb);
			jb.addActionListener(this);
		}
		
		Timer time = new Timer(1000,this);
		time.start();
		jf.add(jp2,BorderLayout.SOUTH);
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new ImageShow();
	}

}
