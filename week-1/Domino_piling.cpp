#include <iostream>
using namespace std;

int max(int n,int m){
if(m>=1&& m<=16 && n>=1&& n<=16){
    return (n*m)/2;
}
return 0;
}
int main(){
    int n,m;
    cin>>n>>m;
    cout<<max(n,m);


}
