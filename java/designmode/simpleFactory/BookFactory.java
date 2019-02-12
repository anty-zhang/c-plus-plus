package designmode.simpleFactory;

public class BookFactory {
	private static IBook getBook(int i) {
		if (1 == i) {
			return new MathBookImp();
		} else if (2 == i) {
			return new EnglishBookImp();
		} else {
			return new EnglishBookImp();
		}
	}
	

	public static void main(String[] args) {
		IBook book = BookFactory.getBook(1);
		book.print();
	}

}
