#Desafios
'''1 Crie um conjunto com os números de 1 a 10 e imprima o conjunto.'''
conjunto = {1,2,3,4,5,6,7,8,9,10}
print(conjunto)

'''2 Crie dois conjuntos, um com os números de 1 a 5 e outro com os números de
3 a 7. Imprima a união, a interseção e a diferença simétrica dos conjuntos.'''
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
conjunto2 = {3,4,5,6,7}
interseccao = conjunto1.intersection(conjunto2)
print(interseccao)

'''3 Crie um conjunto com as vogais (a, e, i, o, u) e peça ao usuário para digitar
uma palavra. Imprima as vogais que aparecem na palavra digitada.'''
conjunto_vogais = ('a','e','i','o','u')
palavra = input("Digite qualquer palavra:")
if 'a' in palavra:
    print("O conjunto contém a vogal a")
if 'e' in palavra:
    print("O conjunto contém a vogal e")
if 'i' in palavra:
    print("O conjunto contém a vogal i")
if 'o' in palavra:
    print("O conjunto contém a vogal o")
if 'u' in palavra:
    print("O conjunto contém a vogal u")

'''4 Crie dois conjuntos com nomes de frutas e verifique se há alguma fruta em
comum entre os conjuntos.'''
conjunto_frutas1 = {'maça','uva','banana','abacaxi','melão','laranja','morango'}
conjunto_frutas2 = {'laranja','morango','pera','kiwi','limão'}
intersecao = conjunto_frutas1.intersection(conjunto_frutas2)
print(intersecao)

'''5 Crie um conjunto com números inteiros aleatórios e imprima o maior e o
menor número do conjunto.'''
conjunto_num_int = {1,12,14,17,24}
minimo = min(conjunto_num_int)
maximo = max(conjunto_num_int)
print(f'O valor minimo do conjunto é: ', minimo, ' e o valor maximo é: ', maximo)

'''6 Crie um conjunto com as cores do arco-íris (vermelho, laranja, amarelo, verde,
azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
digitada está no conjunto e imprima uma mensagem correspondente.'''
conjunto_arco_iris = {'vermelho','laranja','amarelo','verde','azul','anil','violeta'}
cor = input("Digite uma Cor: ")
if 'vermelho' in cor:
    print(f'a cor',cor,'está no arco-iris')
elif 'laranja' in cor:
    print(f'a cor',cor,'está no arco-iris')
elif 'amarelo' in cor:
    print(f'a cor',cor,'está no arco-iris')
elif 'verde' in cor:
    print(f'a cor',cor,'está no arco-iris')
elif 'azul' in cor:
    print(f'a cor',cor,'está no arco-iris')
elif 'anil' in cor:
    print(f'a cor',cor,'está no arco-iris')
elif 'violeta' in cor:
    print(f'a cor',cor,'está no arco-iris')
else :
    print(f'a cor',cor,'não esta no arco-iris')
'''7 Crie um conjunto com os dias da semana (segunda, terça, quarta, quinta,
sexta, sábado, domingo) e remova os dias úteis (segunda a sexta). Imprima o
conjunto resultante.'''
conjunto_dia_semana = {'segunda','terça','quarta','quinta','sexta','sábado','domingo'}
conjunto_dia_semana.remove('segunda','terça','quarta','quinta','sexta')
print(conjunto_dia_semana)
