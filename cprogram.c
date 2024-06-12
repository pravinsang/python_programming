#include<stdio.h>
#include<assert.h>
int fun(int a, int b, int c)
{
    int x = 0;
    int y = 0;
    if(a>0)
        y = 7;
    else
        y = 5;
    if(b>3)
    {
        x = 2;
        if(a <= 0 && c==0)
            y = y-3;
    }
    assert(x + y != 5);
}
int main()
{
    fun(-1, 5, 0);
}