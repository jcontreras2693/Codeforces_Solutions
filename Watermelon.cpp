#include <stdlib.h>
#include <iostream>


using namespace std;

int main(void){
	int weight;
	char Y[5] = "YES";
	char N[5] = "NO";
	cin >> weight;
	if (weight == 2 || weight % 2 != 0) cout << N;
	else cout << Y;
	return 0;
}
