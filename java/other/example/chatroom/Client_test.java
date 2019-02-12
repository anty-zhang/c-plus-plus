package socket.chatroom;

import java.io.*;
import java.net.*;
import java.awt.*;
import java.awt.event.*;

public class Client_test implements ActionListener {
	Frame f;

	TextField tf;

	public Client_test() {
		f = new Frame("welcome");
		f.setLocation(300, 300);
		tf = new TextField("", 20);
		Label l = new Label("请输入用户名称");
		f.add(l, "North");
		f.add(tf);
		tf.addActionListener(this);
		f.pack();
		f.show();
		f.addWindowListener(new WindowAdapter() {
			// 点关闭以后先通知服务器，然后将客户端刷新显示的线程关闭
			public void windowClosing(WindowEvent e) {
				try {
					Thread.sleep(1000);
				} catch (Exception ee) {
					ee.printStackTrace();
				}
				System.exit(1);
			}
		});
	}

	public void actionPerformed(ActionEvent e) {
		String tmp = tf.getText();
		f.dispose();
		new Client(tmp);
	}

	public static void main(String args[]) throws Exception {
		new Client_test();
	}
}