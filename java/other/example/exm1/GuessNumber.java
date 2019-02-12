package day17.high;
/*
作业：
 1 写一个猜数字的游戏，要求：
    点开始按钮生成1-100的随机数，然后猜数字（文本框/按钮），大了提示猜大了（JLabel），小了提示猜小了，对了显示猜的次数。
   文本框得到/设置输入内容方法（getText/setText）
   两个按钮，1个JLabel，1个文本框

  2 试着写一下计算器（不用考虑连加实现）。
 */
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class GuessNumber implements ActionListener{
	JLabel jl = new JLabel("请您产生一个随机数！");
	JTextField jtf = new JTextField(10);
	Random r = new Random();
	int number;
	int count = 1;
	public void actionPerformed(ActionEvent ae){
		String m = ae.getActionCommand();
		if("Random".equals(m)){
			jl.setText("请您猜这个随机数！");
			number = r.nextInt(100);
		}else if("Guess".equals(m)){
			if("".equals(jtf.getText())|| null == jtf.getText()){
				jl.setText("您还没有选择一个随机数！");
			}else{
				int num = Integer.parseInt(jtf.getText());
				if(num==number && number!=0){
					jl.setText("您猜中了这个随机数："+number+"!共猜了"+count+"次");
				}else if(num>number && number!=0){
					jl.setText("大了，继续！");
				}else{
					jl.setText("小了,继续！");
				}
				count++;
			}
			jtf.setText("");
			jtf.requestFocus();//文本框清空
		}
	}
	
	public GuessNumber(){
		JFrame jf = new JFrame("GuessNumber");
		jf.setLayout(new GridLayout(2,1));
		JPanel jp1 = new JPanel();
		jp1.add(jl);
		JButton jb1 = new JButton("Random");
		jb1.addActionListener(this);
		jp1.add(jb1);
		jf.add(jp1);
		
		JPanel jp2 = new JPanel();
		jp2.add(jtf);
		
		JButton jb2=new JButton("Guess");
		jb2.addActionListener(this);
		//jtf.addActionListener(this);//回车监听
		jp2.add(jb2);
		
		jf.add(jp2);
		jf.setSize(400,300);
		//jf.pack();//由jvm自动调节窗口大小
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new GuessNumber();
	}
}
