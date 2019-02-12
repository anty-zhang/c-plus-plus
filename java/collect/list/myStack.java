package collect.list;
import java.util.List;
import java.util.ArrayList;

/*	1. 使用ArrayList实现堆栈功能
 * 	2. list function: isEmpty, add, remove, size
 * 
 */
public class myStack {
	
	private List list = new ArrayList();
	
	public void push(Object obj) {
		list.add(obj);
		System.out.println("push success");
	}
	
	public void pop() {
		if (isEmpty()) {
			System.out.println("list size is empty");
		} else {
			list.remove(list.size() - 1);
			System.out.println("pop success");
		}
	}
	
	public boolean isEmpty() {
		return list.isEmpty();
	}
	
	public void peek() {
		if(isEmpty())
			System.out.println("The stack is empty!");
		else{
			System.out.println(list.get(list.size()-1));
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		myStack myStack = new myStack();
		myStack.push("zhang");
		myStack.push("guo");
		myStack.push("qiang");
		System.out.println("The top of the Stack is:");
		myStack.peek();
		myStack.pop();
		myStack.peek();
		myStack.pop();
		myStack.pop();
		System.out.println(myStack.isEmpty());
		myStack.peek();

	}

}
