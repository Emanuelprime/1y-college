'''1 Escreva uma função recursiva em Python que calcule a soma dos primeiros N
números inteiros positivos.'''


def soma_dos_primeiros_numeros(numero):
    # caso base
    if numero == 1:
        return 1
    # chamada recursiva
    return numero + soma_dos_primeiros_numeros(numero-1)


numero_digitado = int(input('Digite um numero: '))
soma_dos_numeros = soma_dos_primeiros_numeros(numero_digitado)
print(soma_dos_numeros)
input()
'''2 Escreva uma função recursiva para calcular o número fatorial de um número inteiro positivo
'''
def recursividade(numeros2):
    if numeros2 == 1:
        return 1
    else:
        return numeros2 *  recursividade (numeros2 - 1)
numero_digitado2 = int(input('Digite um numero: '))
fatorial = recursividade(numero_digitado2)
print(fatorial)
input()
'''3 Escreva uma função que use uma pilha para inverter uma string.
'''
Pilha = "Galera"
def Reverser(Pilha):
    return Pilha [::-1]
print(Reverser(Pilha))

'''4 Escreva uma função que converte um número decimal em sua representação binária usando uma pilha.'''

