// CPP program for checking of
// Narcissistic number
#include <bits/stdc++.h>
using namespace std;

// function to count digits
int countDigit(int n)
{
    if (n == 0)
        return 0;

    return 1 + countDigit(n / 10);
}

// Returns true if n is Narcissistic number
bool check(int n)
{
    // count the number of digits
    int l = countDigit(n);
    int dup = n;
    int sum = 0;

    // calculates the sum of digits
    // raised to power
    while (dup)
    {
        sum += pow(dup % 10, l);
        dup /= 10;
    }

    return (n == sum);
}

// Driver code
int main()
{
    int n = 1634;
    if (check(n))
        cout << "yes";
    else
        cout << "no";
    return 0;
}
