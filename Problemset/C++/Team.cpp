#include <bits/stdc++.h>

#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)


using namespace std;

int main(void){
    int i, times, cont, solved = 0;
    string problem;
    cin >> times;
    FOR(i,0,times){
        getline(cin >> ws, problem);
        cont = 0;
        FOR(i,0,5){
            if (problem[i] == '1') cont++;
        }
        if (cont >= 2) solved++;
    }
    cout << solved << endl;
    return 0;
}