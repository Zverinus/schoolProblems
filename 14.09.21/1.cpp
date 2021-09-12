#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

ll num;

void printDigits(ll num)
{
	vector<ll> digits;
	while (num)
	{
		ll digit(num % 10);
		digits.push_back(digit);
		num /= 10;
	}

	for (ll i(digits.size() - 1); i >= 0; i--) cout << digits[i] << '\n';
}

int main()
{
	cin >> num;

	printDigits(num);

	return 0;
}