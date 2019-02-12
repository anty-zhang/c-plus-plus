package other.example.national;
import java.util.Scanner;
import java.util.ResourceBundle;
import java.text.MessageFormat;
import java.util.Locale;

public class TestResourceBundle {
	public static void main(String[] args) {
		Locale locale= new Locale("en","US");//ָ���ײ�����Ի���
		System.out.println(locale);
//		for(Locale ll: lc){
//			System.out.println(ll);
//		}
		ResourceBundle rb = ResourceBundle.
			getBundle("test",locale);
		String mes = rb.getString("user.message"); //��Դ�ļ������Ӧ��ֵ
		Scanner sc = new Scanner(System.in);
		String name = sc.next();
		int age = sc.nextInt();
		MessageFormat mf = new MessageFormat(mes);  //��ȡ�õ�ֵ��ʽ��
		Object[] obj = {name,age};     //��Ҫ����Ĳ���д��Object�������ʽ
		String str = mf.format(obj); //��ʽ��obj
		System.out.println(str);
	}

}
