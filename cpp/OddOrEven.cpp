#include <iostream>
using namespace std;

int main()
{
	int n = 0, remainder = 0;

	// Get a number from the keyboard.
	
	cout << "Enter a number and press ENTER: ";
	cin >> n;

	// Get a remainder after dividing by 2.
	
	remainder = n % 2;

	// If remainder is 0, the number input is even.
	
	if (remainder == 0){
		cout << "The number is even." << endl;

	} else {
		cout << "The number is odd" << endl;
	}
	return 0;
}

