#include <iostream>

using namespace std;

int main(int argc, char * argv[])
{
    void *p = NULL;
    int a = 1;
    p = &a;
    cout << "*(int *)p is: " << *(int *)p << " ,sizeof(p) is: " << sizeof(p) << endl;
    double d = 10.0;
    p = &d;
    cout << "*(double *)p is: " << *(double *)p << " ,sizeof(p) is: " << sizeof(p) << endl;

    const char *name = "andy";
    p = (char *) name;
    cout << "*(char*)p is: " << *(char*)p << " ,sizeof(p) is: " << sizeof(p) << endl;

}
