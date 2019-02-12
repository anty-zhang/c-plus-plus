package day18.high;
import javax.swing.*;
import java.awt.event.*;

public class TestMenu implements ActionListener{
	
	JLabel jl = new JLabel();
	public void actionPerformed(ActionEvent ae){
		String mes = ae.getActionCommand();
		jl.setText(mes);
	}
	public TestMenu(){
		JFrame jf = new JFrame("TestMenu");
		JMenuBar jmb = new JMenuBar();
		jf.setJMenuBar(jmb);//
		jf.add(jl);
		String[] menuLab ={"文件","编辑","帮助"};
		JMenu[] jm = new JMenu[menuLab.length];
		String[][] itemLab={{"新建","","保存","另存","打开","","退出"},{"复制","粘贴","剪切","","撤消","删除"},{"关于","欢迎","帮助"}};
		for(int i=0;i<menuLab.length;i++){
			jm[i] = new JMenu(menuLab[i]);
			jmb.add(jm[i]);
			for(int j=0;j<itemLab[i].length;j++){
				if("".equals(itemLab[i][j])){
					jm[i].addSeparator();
				}else{
					JMenuItem jmi = new JMenuItem(itemLab[i][j]);
					jm[i].add(jmi);
					jmi.addActionListener(this);
				}
			}
		}
		
		jf.setSize(300,200);
		jf.setLocation(300,200);
		jf.setVisible(true);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static void main(String[] args) {
		new TestMenu();
	}
}
