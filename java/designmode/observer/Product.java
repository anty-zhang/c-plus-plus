package designmode.observer;

import java.util.Observable;

public class Product extends Observable{
	private String name;
	private double price;
	
	public Product() {
		super();
	}
	public Product(String name, double price) {
		super();
		this.name = name;
		this.price = price;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		System.out.println("===setPrice 1===");
		this.setChanged();		// change = True
		System.out.println("===setPrice 2===");
		this.notifyObservers(price);		// notify
		System.out.println("===setPrice 3===");
		this.price = price;
		System.out.println("===setPrice 4===");
	}
}
