#include<iostream>
using namespace std;
int main()
{
	int x, y;
	cout << "Enter the x and y value:";
	cin >> x >> y;
	if (x > 0 && y > 0)

		if (x >= y)
			cout << "1";
		else
			cout << "2";
	else if (x < 0 && y>0)
		if (abs(x) > y)
			cout << "4";
		else
			cout << "3";
	else if (x < 0 && y < 0)
		if (abs(x) > abs(y))
			cout << "5";
		else
			cout << "6";
	else
		if (x > abs(y))
			cout << "8";
		else
			cout << "7";
	return 0;
}