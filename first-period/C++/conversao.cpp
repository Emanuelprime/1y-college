/*
Inicio
1- Fazer um programa para converter reais para dolares e euros
inicio
definir variaveis com pre-definição de valores para dolar e euro.
solicitar valores em reais para o usuario
calculo com expressoes aritmeticas p/ converter cada moeda
apresentar resultados*/



#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    double valor_reais;
    const float valor_euro {5.63};
    const float valor_dolar{5.25};

    cout<<"Ola, seja bem vindo ao conversor de reais para dolares e euros"<<endl;
    cout<<"Digite o valor em reais para ser convertido: ";
    cin >> valor_reais;
    printf("A conversao de Reais para euro e: %.2f",valor_reais/valor_euro );
    cout<< "A conversao de reais para dolar e: "<<valor_reais/valor_dolar<<endl;





}