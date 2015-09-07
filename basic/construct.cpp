#include <iostream>

using namespace std;

class A {
    private:
        int data;
    public:
        A(const int d):data(d)
        {
            cout << "A(const int d)" << endl;
        }

        //特殊的构造函数，拷贝构造函数
        A(const A &a):data(a.data)
        {
            cout << "A(const A&a)" << endl;
        }
        //A(A a):data(a.data)  // 错误
        //原因：创建对象时要调用构造，调用构造时要创建形参，形参又是一个新对象，创建新对象时又要调用构造，调用构造又要创建形参，…
        //永远也创建不出来新对象

        void show()
        {
            cout << "data=" << data << endl;
        }

        ~A()
        {
            cout << "~A()" << endl;
        }

        friend A add(A a1, A a2);

};

A add(A a1, A a2)  //传obj1不会调用A(int)
{
    int sum = a1.data + a2.data;
    return A(sum);
}

int main(int argc, char * argv[])
{
    A ob1(20);
    A ob2(30);
    add(ob1, ob2).show();
}

//ressult:
//A(const int d)
//A(const int d)
//A(const A&a)
//A(const A&a)
//A(const int d)
//data=50
//~A()
//~A()
//~A()
//~A()
//~A()
//
