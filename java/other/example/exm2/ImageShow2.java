package day18.high;

import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;

public class ImageShow2 implements ActionListener{
	CardLayout cl = new CardLayout();
	JPanel jp1= new JPanel();
	Timer time = new Timer(500,this);
	
	public void actionPerformed(ActionEvent ae){
		String mes = ae.getActionCommand();  //¼ÓÉÏTimer mesÎªnull
		System.out.println(mes);
		if("start".equals(mes)){
			time.start();
		}else if("stop".equals(mes)){
			time.stop();
		}else{
			cl.next(jp1);
		}
	}
	
	public ImageShow2(){
		JFrame jf = new JFrame("ImageShow");
		String[] lab = {"1.jpg","2.jpg","3.jpg","4.jpg"};
		
		
		jp1.setLayout(cl);
		for(int i=0;i<lab.length;i++){
			Icon icon = new ImageIcon("/home/tarena01/"+lab[i]);
			JLabel jl = new JLabel(icon);  
			jp1.add(jl,lab[i]);                   //*****************
		}
		jf.add(jp1,BorderLayout.CENTER);
		
		String[] blab = {"start","stop"};
		JPanel jp2 = new JPanel();
		for(int i=0;i<blab.length;i++){
			JButton jb = new JButton(blab[i]);
			jp2.add(jb);
			jb.addActionListener(this);
		}
		
		//time.start();
		//if("stop".equals(mes)){
			//time.stop();
		//}
		jf.add(jp2,BorderLayout.SOUTH);
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new ImageShow2();
	}

}
