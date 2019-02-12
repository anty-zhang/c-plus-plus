#include <iostream>

using namespace std;

int main(int argc, char * argv[])
{
    char *p = "andy-zhang";
    cout << "p=" << p << endl;
    cout << "===============" << endl;
    for (int i = 0 ; i < strlen(p); i++)
    {
        cout << p + i << endl;
    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////
//ressult:
//p=andy-zhang
//===============
//andy-zhang
//ndy-zhang
//dy-zhang
//y-zhang
//-zhang
//zhang
//hang
//ang
//ng
//g
////////////////////////////////////////////////////////////////////////////////////////////////////
