'''Implemente uma função is_paliindrome que recebe uma string
como parâmetro e retorna True se a string é um palíndrome e False caso
contrário. Um palíndrome é uma palavra, frasem número ou qualquer outra
sequência de caracteres que é lida da mesma forma tanto da esquerda para
a direita como para esquerda. Exemplos de palíndromos incluem "arara", "radar", "12321"
'''
palindromo = str(input("Insira uma palavra qualquer:").replace(" ", ""))
pilha = []
def push(lista, palavra):
    return lista.append(palavra)
for i in palindromo:
    push(pilha, i)

def verificaPalindrome(palindromo):
    if (palindromo == palindromo[::-1]):
        print("É um palíndromo")
    else:
        print("Não é palíndromo")

verificaPalindrome(palindromo)
print(pilha)

