package socket.chatroom;

import java.awt.*;
import java.awt.event.*;

public class Server_frame extends WindowAdapter implements ActionListener {
	private Frame server_frame;

	private Panel pan;

	private MenuBar menu_bar;

	private TextArea server_text;

	private Server_socket ss;

	// 创建server窗口
	public void fix_server() {
		server_frame = new Frame("Server Frame");
		server_frame.addWindowListener(this);
		server_frame.setLocation(300, 200);
		server_frame.setSize(350, 350);

		menu_bar = new MenuBar();
		server_frame.setMenuBar(menu_bar);

		Menu Admin = new Menu("Admin");
		MenuItem Star = new MenuItem("Star");
		Star.addActionListener(this);
		MenuItem Stop = new MenuItem("Stop");
		Stop.addActionListener(this);
		MenuItem exit = new MenuItem("exit");
		exit.addActionListener(this);
		Admin.add(Star);
		Admin.add(Stop);
		Admin.add(exit);
		Menu show = new Menu("show");
		MenuItem Connect = new MenuItem("Connect");
		MenuItem ConnectIP = new MenuItem("ConnectIP");
		show.add(Connect);
		show.add(ConnectIP);
		Menu help = new Menu("help");
		menu_bar.add(Admin);
		menu_bar.add(show);
		menu_bar.add(help);

		pan = new Panel();
		pan.setBackground(Color.pink);
		server_frame.add(pan, BorderLayout.CENTER);
		server_text = new TextArea(18, 45);
		server_text.setBackground(Color.white);
		server_text.setEditable(false);
		pan.add(server_text, BorderLayout.CENTER);

		server_frame.setResizable(false);
		server_frame.setVisible(true);

	}

	// 事件处理
	public void windowClosing(WindowEvent e) {
		System.exit(0);
	}

	public void actionPerformed(ActionEvent e) {
		String s = e.getActionCommand();
		if (s.equals("Star")) {
			System.out.println("Star is click");
			ss = new Server_socket();
			ss.start();
		} else if (s.equals("Stop")) {
			ss.stop_server();
			System.out.println("Stop is click");

		} else if (s.equals("exit")) {
			System.exit(0);
		}
	}
}