#include <iostream>
#include <vector>
using namespace std;
int main(){
    // vector <char> vogais

    vector<char> vogais {'a','b','c','d','e'};

    cout<<vogais[0]<<endl;
    cout<<vogais[2]<<endl;

    vector<int> pontuacao {10,98,89};
    cout<<"pontuacao utilizando sintax  vetorial"<<endl;
    cout<<pontuacao.at(0)<<endl;
    cout<<pontuacao.at(2)<<endl;


cout<<" existem "<< pontuacao.size()<<"pontuacoes no vetor"<<endl;

cout<<"\n Digite uma nova pontuacao para add ao vetor"<<endl;
int pontuacao_add{0};
cin>>pontuacao_add;

pontuacao.push_back(pontuacao_add);

cout<<"Insira mais um valor no vetor"<<endl;
cin>>pontuacao_add;
pontuacao.push_back(pontuacao_add);

cout<<"as pontuacoes ate entao"<<endl;
cout<<pontuacao.at(0);
cout<<pontuacao.at(1);
cout<<pontuacao.at(2);
cout<<pontuacao.at(3);
cout<<pontuacao.at(4);






    return 0;
}