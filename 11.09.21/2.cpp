#include <iostream>

using namespace std;

int maxN(0), counter(0);
long long sum(0);

int main()
{
	for (int i(2381); i <= 14655; i++)
	{
		if ((i % 6 == 0 || i % 11 == 0) && i % 5 != 0 && i % 7 != 0 && i % 1000 / 100 != i % 100 / 10)
		{
			counter++;
			sum += i;
			maxN = i;
		}
	}
	cout << sum / counter << " " << maxN;
	return 0;
}