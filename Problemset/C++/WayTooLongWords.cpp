#include <stdlib.h>
#include <iostream>


using namespace std;

int main(void){
	int times, i;
	cin >> times;
	string word;
	for (i = 0; i < times; i++){
		cin >> word;
		int len = word.length();
		if (len > 10) cout << word[0] << len - 2 << word[len - 1] << '\n';
		else cout << word << '\n';	
	}
	return 0;
}
 