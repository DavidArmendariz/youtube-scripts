#include<iostream>
#include<vector>
using namespace std;

void coding_challenge3(vector<int> x){
	int count = 0;
	int n = x.size();
	for(int i=1;i<=n-2;i++){
		if(x[i-1]==1 && x[i] == 1 && x[i+1]==0){
			count++;
		}
		if(i==n-2 && x[i] == 1 && x[i+1] == 1){
			count++;
		}
	}
	cout << "Number of blocks of 1s: " << count << endl;
}
int main(){
	vector<int> x;
	cout << "Enter the numbers of the vectors or -1 to quit\n" << endl;
	int a;
	do{
		cin >> a; 
		if(a==-1){
			break;
		}
		x.push_back(a);
	}while(true);
	coding_challenge3(x);
}
