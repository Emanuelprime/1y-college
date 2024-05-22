/*
Inicio
1- Fazer um programa que pergunte um valor em metros e imprima o correspondente em decímetros, centímetros e milímetros.
pre definir milimetros, decimetro e centimetro
solicitar valor de metro
calcular
resltado
*/

#include <iostream>
using namespace std;
int main(){
    double metro;
    double cent {100};
    double dec {10};
    double mil {1000};
    cout<<"Seja bem vindo ao conversor de metros para decimetro, centimetro ou milimetro"<<endl;
    cout<<"Defina o valor que deseja converter em metros: "<<endl;
    cin>>metro;
    cout<<"O valor de metros para centimetro e: "<<metro*cent<<" cm"<<endl;
    cout<<"O valor de metros para milimetro e: "<<metro*mil<<" mm"<<endl;
    cout<<"O valor de metros para decimetro e: "<<metro*dec<<" dm"<<endl;
}