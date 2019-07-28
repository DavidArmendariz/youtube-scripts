#include<iostream>
#include<string>
#include<cmath>
using namespace std;

void narcisistas(int n){
	for(int i=0;i<=n;i++){
		string j = to_string(i);
		int p = j.length();
		int s = 0;
		for(int k=0;k<p;k++){
			int d = j[k] - '0';
			s += pow(d,p);
		}
		if(s==i){
			cout << i << endl;
		}
	}
}

int main(){
	int n;
	cout << "Ingrese n:" << endl;
	cin >> n;
	narcisistas(n);
}
