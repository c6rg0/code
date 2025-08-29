/* This has no use case now,
 * just a fancy template if something breaks */



#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int rand_xtox(int n);

int main()
{
	int n = 0;
	int r = 0;
	int i = 1;

	srand(time(nullptr)); // set seed for randomizing
	cout << rand << "rand";
	cout << "Enter number of dice to roll > ";
	cin >> n;

	for (;i <= n; ++i){
		r = rand_xtox(6) + 1; // get a number 1 - 6
		cout << r << " "; // print it
		}
	return 0;
}
// Random 0 to N1 function.
int rand_xtox(int n){
	return rand() % n;
}
