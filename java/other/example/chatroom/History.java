package socket.chatroom;

import java.io.Serializable;

public class History implements Serializable {
	public String wang = "";

	public void setWord(String b) {
		this.wang = b + "\n" + this.wang;
	}

	public String getWord() {
		return this.wang;
	}
}