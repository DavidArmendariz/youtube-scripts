#include<iostream>
#include<vector>
#include<cstdlib>
#include<numeric>
#include<bits/stdc++.h>
using namespace std;
void coding_challenge1(vector<int> x){
	vector<int> y; vector<int> s;
	int n = x.size();
	for(int i=0;i<n-1; i++){
		if(x[i]<x[i+1]){
			y.push_back(x[i]);
			if(i==n-2){
				y.push_back(x[i+1]);
				s.push_back(accumulate(y.begin(),y.end(),0));
				for(int i=0;i<y.size();i++){
					cout << y[i] << " ";
				}
			}
			continue;
		}
		else if(x[i] >= x[i+1] && x[i] > x[i-1]){
			y.push_back(x[i]);
			s.push_back(accumulate(y.begin(),y.end(),0));
			for(int i=0;i<y.size();i++){
				cout << y[i] << " ";
			}
			cout << endl;
			y.clear();
		}
	}
	cout << endl << "Sumas de la secuencia" << endl;
	for(int i=0;i<s.size();i++){
		cout << s[i] << endl;
	}
	cout << "Suma maxima" << endl << *max_element(s.begin(),s.end());
}

int main(){
	vector<int> m;
	cout << "Ingrese los numeros o escriba 'q' para salir: " << endl;
	string c;
	do{
		getline(cin,c);
		if(c=="q"){
			break;
		}
		else{
			m.push_back(atoi(c.c_str()));
		}
	}while(true);
	coding_challenge1(m);
	return 0;
}
