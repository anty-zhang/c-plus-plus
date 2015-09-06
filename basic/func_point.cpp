#include <iostream>

using namespace std;
void show(int input[], int n);
void reset(int input[], int n);

int main(int argc, char * argv[])
{
    int a[] = {1, 2, 3, 4, 5};
    show(a, 5);
    void (*fp)(int [], int) = NULL;
    fp = show;
    fp(a, 5);
    cout << "=======================" << endl;
    fp = reset;
    fp(a, 5);
    fp = show;
    fp(a, 5);
}

void show(int input[], int n)
{
    for (int i = 0 ; i < n ; i++)
        cout << input[i] << " ";
    cout << endl;
}

void reset(int input[], int n)
{
    memset(input, 0, sizeof(int) * n);
}


////////////////////////////////////////////////////////////////////////////////////////////////
//result:
//1 2 3 4 5
//1 2 3 4 5
//=======================
//0 0 0 0 0
//
////////////////////////////////////////////////////////////////////////////////////////////////

