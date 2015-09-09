#include <iostream>

using namespace std;

// 指针实现动态内存


class Array {
    private:
        char *p;
        int len;
    public:
        //construct
        Array(int len):len(len),p(new char[len])
        {
            cout << "construct Array(int len)" << endl;
        }

        //copy construct
        Array(const Array &a):len(a.len)
        {
            cout << "copy construct Array(const Array &a)" << endl;
            p = new char[len];
            for (int i = 0 ; i < len ; i ++)
            {
                p[i] = a.p[i];
            }
        }

        void fill(char start, int n)
        {
            for (int i = 0 ; i < len ; i ++)
            {
                p[i] = start + i * n;
            }
        }

        void show()
        {
            for (int i = 0 ; i < len ; i ++)
            {
                cout << p[i] << " ";
            }
            cout << endl;
        }

        // destruct
        ~Array()
        {
            cout << "destruct ~Array" << endl;
            delete []p;
            p = NULL;
        }
};

int main(int argc, char * argv [])
{
    Array a1(5);
    a1.fill('a', 1);
    a1.show();
    cout << "================" << endl;
    Array a2(a1);
    a2.show();
    a2.fill('A', 1);
    a2.show();
    a1.show();

}


//result:
//construct Array(int len)
//a b c d e
//================
//copy construct Array(const Array &a)
//a b c d e
//A B C D E
//a b c d e
//destruct ~Array
//destruct ~Array
//
