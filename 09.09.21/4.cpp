#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

ll num1, num2, counter(0);

ll gcd(ll a, ll b)
{
	if (b == 0) return a;
	counter++;
	return gcd(b, a % b);
}

int main()
{
	cin >> num1 >> num2;
	cout << "gcd " << gcd(num1, num2) << "\n";
	cout << "steps " << counter;
	return 0;
}