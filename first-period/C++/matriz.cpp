#include <iostream>
using namespace std;
int main(){

int n1 [0]
 int n2 [4] {100, 800, 500, 60}

char vogais [] {'a','e','i','o','u'};
cout<<"A primeira vogal eh: "<<vogais[0]<<endl;
cout<<"A ultima vogal eh: "<<vogais[4]<<endl

double temperatura [] {90.1,89.8,77.5,81.6};
cout<<"\nA primeira temperatura eh: "<<temperatura[0];

temperatura[0] = 100.7;

int pontuacao [5]{100,90,80,70,60};

cout<<"primeira pontuacao: "<<pontuacao[0]<<endl;
cout<<"segunda pontuacao: "<<pontuacao[1]<<endl;
cout<<"terceira pontuacao: "<<pontuacao[2]<<endl;
cout<<"quarta pontuacao: "<<pontuacao[3]<<endl;
cout<<"quinta pontuacao: "<<pontuacao[4]<<endl;

cout<<"\nDigite 5 pontuacoes: "<<endl;
cin>>pontuacao [0];
cin>>pontuacao [1];
cin>>pontuacao [2];
cin>>pontuacao [3];
cin>>pontuacao [4];

cout<<"primeira pontuacao: "<<pontuacao[0]<<endl;
cout<<"segunda pontuacao: "<<pontuacao[1]<<endl;
cout<<"terceira pontuacao: "<<pontuacao[2]<<endl;
cout<<"quarta pontuacao: "<<pontuacao[3]<<endl;
cout<<"quinta pontuacao: "<<pontuacao[4]<<endl;



//declarando uma matriz de tamanho fixo 3x3

int matriz [3] [3];
// inicializando a matriz com valores

matriz [0][0] =1;
matriz [0][1] =2;
matriz [0][2] =3;
matriz [1][0] =4;
matriz [1][1] =5;
matriz [1][2] =6;
matriz [2][0] =7;
matriz [2][1] =8;
matriz [2][2] =9;

//acessando e exibindo os elementos da matriz
    for (int i = 0; i <3;i++){
        for (int j = 0; j<3; j++){
        cout<<matriz [i][j]<<" ";
} 
cout<<endl;
}


}