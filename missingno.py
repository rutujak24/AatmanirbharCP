#   https://practice.geeksforgeeks.org/problems/missing-number/0
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    long long sum=0;
	    int temp;
	    for(int i=0; i<n-1; i++){
	        cin>>temp;
	        sum+=temp;
	    }
	    long long idealSum=n*(n+1)/2;
	    cout<<idealSum-sum<<endl;
	}
	return 0;
}