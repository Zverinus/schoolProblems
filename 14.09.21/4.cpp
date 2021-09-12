#include <iostream>
#include <cmath>

using namespace std;
typedef long long ll;

ll a, b;

bool isPrime(ll num)
{
	if (num == 0 || num == 1) return false;
	if (num == 2) return true;
	if (num % 2 == 0) return false;
	for (ll i = 3; i <= sqrt(num); i += 2) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}

int main()
{
	cin >> a >> b;

	for (ll i(a); i <= b; i++)
	{
		if (isPrime(i)) cout << i << '\n';
	}
	return 0;
}