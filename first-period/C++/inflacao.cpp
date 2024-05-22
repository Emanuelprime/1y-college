/*
Inicio
1- Fazer um programa que lê o preço de um produto e inflacione o preço em 10% se ele for menor que 100 reais e em 20% se for maior ou igual a 100 reais.
solicite preço do produto
calcular
resultado*/


#include <iostream>
using namespace std;
int main(){
    double valor_produto;

    const double taxa_menor {0.1};
    const double taxa_maior_igual {0.2};
    cout<<"seja bem vindo ao projeto inflacao ";
    cout<<"Defina o valor do produto"<<endl;
    cin>>valor_produto;
    if (valor_produto < 100){
        valor_produto = valor_produto+valor_produto*taxa_menor;
        cout<<valor_produto;
    }
    else {
        valor_produto = valor_produto+valor_produto*taxa_maior_igual;
        cout<<valor_produto;
    }
}