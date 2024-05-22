/* 
Inicio
1- fazer um programa que descobre a idade pelo ano de nascimento e ano atual
definir variavel com pre-definição de valor para ano atual
solicitar ano de nascimento
calcular ano atual menos ano de nascimento*/

#include <iostream>
using namespace std;
int main(){
    int ano_atual;
    int ano_nascimento;
    cout<<"seja bem vindo a calculadora de idade."<<endl;
    cout<<"Defina o ano atual: "<<endl;
    cin>>ano_atual;
    cout<<"Defina o ano do seu nascimento: "<<endl;
    cin>>ano_nascimento;
    cout<<"========================================"<<endl;
    cout<<"Sua idade e: "<<ano_atual-ano_nascimento<<endl;
    cout<<"========================================";
}