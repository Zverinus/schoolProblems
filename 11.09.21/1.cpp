#include <iostream>

using namespace std;

int counter(0), minN(0);

int main()
{
	for (int i(10153); i >= 4413; i--)
	{
		short tens = i % 100 / 10;
		if (i % 5 == 0 && i % 23 == 0 && i % 7 != 0 && i % 10 != 0 && (tens == 1 || tens == 2 || tens == 3))
		{
			counter++;
			minN = i;
		}
	}
	cout << counter << " " << minN;
	return 0;
}