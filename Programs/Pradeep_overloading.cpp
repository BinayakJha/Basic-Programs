#include <iostream>
using namespace std;

class complex
{
    private:
    int real,imaginary;

    public:
    complex(){}
    void setData(int x,int y)
    {
        real = x;
        imaginary = y;
    }

    void showData()
    {
        cout<<real<<"  +  "<<imaginary<<"i"<<endl;

    }

    complex operator+(complex c2);
    complex operator-(complex c2);
    complex operator*(complex c2);
    friend complex operator++(complex &c2);
    friend complex operator--(complex &c2);
    friend complex operator+(complex c1,int x);
    complex operator+=(complex &c2);
};

complex complex :: operator+=(complex &c)
{
    real = c.real + real;
    imaginary = c.imaginary + imaginary;
}

complex operator++(complex &c2)
{
    c2.real++;
    c2.imaginary++;
    return c2;
}

complex operator--(complex &c2)
{
    c2.real--;
    c2.imaginary--;
    return c2;
}
complex complex :: operator +(complex c2)
    {
        complex temp;
        temp.real = c2.real + real;
        temp.imaginary = c2.imaginary + imaginary;
        return temp;
    }

complex complex :: operator-(complex c2)
{
    complex temp;
    temp.real = real - c2.real;
    temp.imaginary = imaginary - c2.imaginary;
    return temp;
}

complex complex :: operator *(complex c2)
    {
        complex temp;
        temp.real = c2.real * real;
        temp.imaginary = c2.imaginary * imaginary;
        return temp;
    }

complex operator+(complex c1,int x)
{
    complex temp;
    temp.real = c1.real + x;
    temp.imaginary = c1.imaginary + x;
    return temp;
}
int main()
{
    complex c1,c2,c3;
    c1.setData(2,5);
    c1.showData();
    c2.setData(5,7);
    c2.showData();
    // c3 = c1 + c2;
    // c3.showData();
    // c3 = c2 - c1;
    // c3.showData();
    // c3 = c1*c2;
    // c3.showData();
    // c3 = c1 + 30;
    // c3.showData();
    // ++c3;
    // c3.showData();
    // --c3;
    // c3.showData();
    c3+=c1;
    c3.showData();
}