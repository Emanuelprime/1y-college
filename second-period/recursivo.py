'''def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)
x = int(input("Informe um valor:"))
print("Fatorial: ", fatorial(x))

Teste de mesa (numero 5)
(1)fatorial(5) = 5*fatorial 4 -> 120
(2)fatorial(4) = 4*fatorial 3 -> 24
(3)fatorial(3) = 3*fatorial 2 -> 6
(4)fatorial(2) = 2*fatorial 1 -> 2
(5)fatorial(1) = 1


#Somar - Recursivo
def somar (numero):
    #caso base
    if numero == 1:
        return 1
    #chamada recursiva
    return numero + somar(numero-1)

x = int(input("Informe um valor:"))
print("Soma: ", somar(x))'''

#Fibonacci Recursivo
def fibonacci(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 1
    else:
        return fibonacci(posicao-1) + fibonacci(posicao-2)
x = int(input("Informe um valor:"))
print("Fibonnaci: ", fibonacci(x))
