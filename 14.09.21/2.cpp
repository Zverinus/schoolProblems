#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

ll num;

void printDivs(ll num)
{
	for (ll i(1); i <= num / 2; i++)
	{
		if (num % i == 0) cout << i << ' ';
	}
	cout << num;
}

int main()
{
	cin >> num;

	printDivs(num);

	return 0;
}