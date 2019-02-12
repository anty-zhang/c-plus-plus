#include <iostream>

using namespace std;

// 构造函数析构函数执行顺序

class Int {
    public:
        Int()
        {
            cout << "Int()" << endl;
        }
        ~Int()
        {
            cout << "~Int()" << endl;
        }
};

class A {
    private:
        int n;
        Int obj;
    public:
        A(int n = 0):n(n)
        {
            cout << this << "A(" << n << ")" << endl;
        }
        ~A()
        {
            cout << this << "~A(" << n << ")" << endl;
        }

};

void fun()
{
    A a3(3);
    static A a4(4);    //静态对象只首次执行
}

int main(int argc, char * argv[])
{
    fun();
    fun();
    A a2(2);

}

A a1(1);   //全局对象最先调用


// result:
// Int()
// 0x10eaa7148A(1)
// Int()
// 0x7fff5115ab18A(3)
// Int()
// 0x10eaa7138A(4)
// 0x7fff5115ab18~A(3)
// ~Int()
// Int()
// 0x7fff5115ab18A(3)
// 0x7fff5115ab18~A(3)
// ~Int()
// Int()
// 0x7fff5115ab38A(2)
// 0x7fff5115ab38~A(2)
// ~Int()
// 0x10eaa7138~A(4)
// ~Int()
// 0x10eaa7148~A(1)
// ~Int()
