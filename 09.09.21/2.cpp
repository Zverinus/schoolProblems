#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

ll num;
bool hasSame(false);
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

	for (ll i(0); i < digits.size() - 1; i++)
	{
		if (digits[i] == digits[i + 1])
		{
			hasSame = true;
			break;
		}
	}

	cout << (hasSame ? "NO" : "YES");

	return 0;
}