package basic.compare;

/*
 * overload hashCode
 * overload	equals
 * overload	toString
 * overload compareTo
 */
public class Student implements Comparable<Student> {

	private int id;
	private String name;
	
	public Student() {
		super();
	}
	
	public Student(int id, String name) {
		super();							// call super
		this.setId(id);
		this.setName(name);
	}
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public int compareTo(Student o) {
		System.out.println("this id: " + id + " compare id: " + o.getId());
		if (null == o) {
			return 0;
		}
		return this.getId() - o.getId();
	}
	
	@Override
	public String toString() {
		return "Student [id=" + id + ", name=" + name + "]";
	}

	@Override
	public int hashCode() {
		System.out.println("hash: " + getId());
		final int prime = 31;
		int result = 1;
		result = prime * result + id;
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		System.out.println("equals: " + getId());
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Student other = (Student) obj;
		if (id == other.id)
			return true;
		else
			return false;
	}

}
