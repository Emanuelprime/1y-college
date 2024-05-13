'''
Operadores aritmeticos
Adição -> +
Subtração -> -
Multiplicação -> *
Divisão -> /
Exponenciação -> **
Parte inteira -> //
Modulo/Mod/Resto da divisão -> %
'''

#Entrada e Saída
'''print("Digite seu nome:")
nome= input()
print("Bem-vindo(a),", nome)'''

'''
Operadores de comparação 
== -> igualdade 
!= -> diferente
> -> maior
>= -> maior ou igual
< -> menor
<= -> menor ou igual
'''

#Estruturas Condicionais simples
'''a = 6
b = 4
soma =  a + b

if soma >= 10 :
    print("O valor da soma é:", soma)
else:
    print("Valor falso do teste")'''

'''
Operadores logicos
AND -> e
OR -> ou
NOT -> não
'''
'''x = 3.5
y = 1.2

if y< x and x > 3:
    print("As duas condições são verdadeiras")
else:
    print("Pelo menos uma condição ou as duas são falsas")'''

#Estrutura Condicional Composta

'''temperatura = float(input("Informe a temperatura:"))

if temperatura >= 30:
    print("Muito calor!")
elif temperatura >= 24:
    print("Calor")
elif temperatura >= 17:
    print("Temperatura Amena")
elif temperatura >= 7:
    print("Temperatura Fria")
else:
    print("Muito fria")'''

'''numero = int(input("Informe um valor:"))

if numero % 2 == 0 and numero != 0:
    print(f'{numero} é par')
elif numero % 2 !=0:
    print(f'{numero} é impar')
else:
    print(f'{numero} é zero')'''

#Estrutura de Repetição
#variavel acumuladora
acumuladora = 0
for i in range(10):
    nota1 = float(input("Informe nota1:"))
    nota2 = float(input("Informe nota2:"))
    media = (nota1 + nota2) / 2
    print("A média do aluno é : {0:.2f".format(media))
    acumuladora = acumuladora + media
mediaGeral = acumuladora / 10
print("A meédia da turma é: {0:.2f}".format(mediaGeral))
