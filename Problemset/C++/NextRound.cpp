#include <bits/stdc++.h>

#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)


using namespace std;

int main(void){
    int i, n, k, cont = 0, j = 0;
    cin >> n >> k;
    string p, places[n], temp;
    getline(cin >> ws, p);
    FOR(i,0,p.length()){
        if (p[i] != ' ') temp+= p[i];
        else{
            places[j] = stoi(temp);
            j++;
            temp.clear();
        }
        if (i == p.length() - 1) places[j] = stoi(temp);
    }
    temp = stoi("0");
    FOR(i,0,n){
        if (places[i] >= places[k - 1] && places[i] != temp) cont++;
        //if (places[i] >= places[k - 1]) cont++;
    }
    cout << cont << endl;
    return 0;
}