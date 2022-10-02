#include<iostream>
using namespace std; 

int fact(int num)
{ if(num<=1)
   return 1;                        //Factoroial Function
else
   return num*fact(num-1);
}

bool check(int number)
{ int n=number;
  int sum=0;
	while(n!=0)
	{
		int remainder=n%10;       //Gets the remainder, thereby taking each digit of the number
		n=n/10;
		sum=sum+fact(remainder); //adding the factorials of each number
	}
	if(sum==number) //if that factorial sum is equal to the given number, then it returns true
	return true;
	else
	return false;
}

void strongnum(int range)
{
	for(int i=1;i<range;i++)
	{
		if(check(i))
		cout<<i<<" ";
	}
}




int main()
{ //Take the value upto which you want to print all the Strong Numbers from 0 as the starting point.
	int range;
	cin>>range;
	strongnum(range);
}
