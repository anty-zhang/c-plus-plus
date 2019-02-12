package socket.chatroom;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

/**
 * 客户端的程序,完成客户端屏幕的刷新
 * 
 * @Author zhang
 * @Date 2005-04-16
 * @version 1.0
 */
public class Client extends Thread implements ActionListener {
	private TextArea ta;

	private TextField tf;

	private Frame f;

	private Button b1;

	private Panel p;

	private String name;

	private Socket socket;

	private DataInputStream in;

	private DataOutputStream out;

	private String temp = ""; // 用于比较两次输入是否相同

	private boolean flag = true; // 用于判断是否需要刷新客户端的TEXTAREA显示

	/**
	 * 构造器，记录客户的NAME和完成界面的初始化，同时调用INIT方法
	 * 
	 * @param name
	 *            客户名称
	 * @Author zhang
	 * @Date 2005-04-16
	 */
	public Client(String name) {
		// 记录登陆者的名字
		this.name = name;
		f = new Frame("client frame");
		f.setLocation(300, 300);
		ta = new TextArea(20, 60);
		tf = new TextField("", 40);
		b1 = new Button("send");
		p = new Panel();
		ta.setEditable(false);
		p.add(tf);
		p.add(b1);
		f.add(p, BorderLayout.NORTH);
		f.add(ta, BorderLayout.CENTER);
		f.pack();
		f.show();
		init();
	}

	/**
	 * 完成SOCKET连接以及注册监听，同时启动线程
	 * 
	 * @Author zhang
	 * @Date 2005-04-16
	 */
	private void init() {
		try {
			socket = new Socket("127.0.0.1", 2222);
			in = new DataInputStream(socket.getInputStream());
			out = new DataOutputStream(socket.getOutputStream());
			// 发送登陆者名字，并读取服务端的信息
			out.writeUTF("<1.1>");// 通知服务器,有新人登陆
			out.writeUTF(name);// 发送新人的用户名
			out.writeUTF("<2.1>");// 请求服务器发送全部聊天信息
			ta.setText(in.readUTF());
		} catch (Exception ee) {
			// 出现SOCKET异常就退出
			ee.printStackTrace();
			System.exit(1);
		}
		// 注册监听
		tf.addActionListener(this);
		b1.addActionListener(this);
		f.addWindowListener(new WindowAdapter() {
			// 点关闭以后先通知服务器，然后将客户端刷新显示的线程关闭
			public void windowClosing(WindowEvent e) {
				try {
					out.writeUTF("<3.2>");// 有人离开
					flag = false;
					Thread.sleep(2000);
				} catch (Exception ee) {
					ee.printStackTrace();
				}
				System.exit(1);
			}
		});
		this.start();
	}

	/**
	 * 监听处理方法，主要是将客户说的话提交到服务器端，同时更新客户端的显示
	 * 
	 * @Author zhang
	 * @Date 2005-04-16
	 */
	public void actionPerformed(ActionEvent e) {
		// 判断是否和上句话相同，防止用回车刷屏
		if (tf.getText() != null && (!temp.equals(tf.getText()))) {
			temp = tf.getText();
			try {
				out.writeUTF("<2.2>");// 代表客户正常说话
				out.writeUTF(tf.getText());
				out.writeUTF("<2.1>");
				ta.setText(in.readUTF());
				// 发送信息后清空TF，同时TF获得光标焦点
				tf.setText("");
				tf.requestFocus();
			} catch (Exception ee) {
				ee.printStackTrace();
			}
		}
	}

	/**
	 * 线程的方法体，功能是每隔半秒更新客户端的显示
	 * 
	 * @Author zhang
	 * @Date 2005-04-16
	 */
	public void run() {
		// 用FLAG判断客户端是否需要刷新屏幕
		while (flag) {
			try {
				Thread.sleep(500);
				out.writeUTF("<2.1>");// 要求刷新屏幕
				ta.setText(in.readUTF());
			} catch (Exception ee) {
				// 出现异常代表服务器出现问题，客户端提示后退出
				ee.printStackTrace();
				ta.setText("服务器出现错误，本窗口3秒后关闭。");
				try {
					Thread.sleep(3000);
				} catch (Exception ea) {
					ea.printStackTrace();
				}
				System.exit(1);
			}
		}
	}

}