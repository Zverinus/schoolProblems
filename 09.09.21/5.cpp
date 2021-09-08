#include <iostream>

using namespace std;
typedef long long ll;

ll num, counter(0);


int main()
{
	cin >> num;
	while (num != 0)
	{
		if (num % 3 == 0) counter++;
		cin >> num;
	}
	cout << counter;
	return 0;
}