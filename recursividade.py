'''1 Escreva uma função recursiva em Python que calcule a soma dos primeiros N
números inteiros positivos.'''


def soma_dos_primeiros_numeros(valor):
    # caso base
    if valor == 1:
        return 1
    # chamada recursiva
    return valor + soma_dos_primeiros_numeros(valor-1)


numero_digitado = int(input('Digite um valor: '))
soma_dos_numeros = soma_dos_primeiros_numeros(numero_digitado)
print(soma_dos_numeros)


'''2 Escreva uma função recursiva para calcular o número fatorial de um número inteiro
positivo.'''
def fatorial(numeros):
    if numeros == 0:
        return 1
    else:
        return numeros * fatorial(numeros - 1)  
valor = int(input("Digite um valor inteiro positivo: "))

if valor < 0:
    print("O fatorial não está definido para números negativos.")
else:
    resultado = fatorial(valor)
    print(f"O fatorial de {valor} é {resultado}.")