#include <iostream>
using namespace std;
int main(){
    const int tamanho =5;
string matriz[tamanho][2];
for (int i = 0; i < 5 ; i++)
{
    
    cout<<"Digite seu nome"<<'\n';
    cin>>matriz[i][0];
    cout<<"Digite seu cpf"<<'\n';
    cin>>matriz[i][1];
} 
for (int i = 0; i < 5 ; i++)
{
   cout<<matriz[i][0]<<'\n';
   cout<<matriz[i][1]<<'\n';
}


      
return 0;
}