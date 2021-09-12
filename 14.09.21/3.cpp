#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

ll num;

void printFibbs(ll num)
{
	vector<ll> fibbs{ 1, 1 };
	if (num == 1)
	{
		cout << 1;
		return;
	}
	cout << 1 << ' ' << 1 << ' ';
	fibbs.resize(num);
	for (ll i(2); i < num; i++)
	{
		fibbs[i] = fibbs[i - 1] + fibbs[i - 2];
		cout << fibbs[i] << ' ';
	}
}
int main()
{
	cin >> num;

	printFibbs(num);

	return 0;
}