#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

ll num, counter(0);
vector<ll> digits;

int main()
{
	cin >> num;

	while (num)
	{
		ll digit(num % 10);
		digits.push_back(digit);
		num /= 10;
	}

	sort(digits.begin(), digits.end());

	for (auto digit : digits)
	{
		if (digit == 1) counter++;
	}

	cout << counter;

	return 0;
}