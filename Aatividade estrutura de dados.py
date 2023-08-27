#Desafios
# 1. Crie um conjunto com os números de 1 a 10 e imprima o conjunto.
print("1-conjunto com os números de 1 a 10")
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(conjunto)
input()

# 2. Crie dois conjuntos, um com os números de 1 a 5 e outro com os números de 3 a 7. Imprima a união, a interseção e a diferença simétrica dos conjuntos.
print("2-União, interseção e dif simetrica ")
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
interseccao = conjunto1.intersection(conjunto2)
uniao = conjunto1 | conjunto2
dif_simetr = conjunto1 ^ conjunto2
print("Interseção")
print(interseccao)
print("União")
print(uniao)
print("Diferença simétrica")
print(dif_simetr)
input()

# 3. Crie um conjunto com as vogais (a, e, i, o, u) e peça ao usuário para digitar uma palavra. Imprima as vogais que aparecem na palavra digitada.
print("3-Vogais")
conjunto_vogais = ('a', 'e', 'i', 'o', 'u')
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
input()

# 4. Crie dois conjuntos com nomes de frutas e verifique se há alguma fruta em comum entre os conjuntos.
print("4-Frutas")
conjunto_frutas1 = {'maça', 'uva', 'banana', 'abacaxi', 'melão', 'laranja', 'morango'}
conjunto_frutas2 = {'laranja', 'morango', 'pera', 'kiwi', 'limão'}
intersecao = conjunto_frutas1.intersection(conjunto_frutas2)
print(intersecao)
input()

# 5. Crie um conjunto com números inteiros aleatórios e imprima o maior e o menor número do conjunto.
print("5-Maior e Menor")
conjunto_num_int = {1, 12, 14, 17, 24}
minimo = min(conjunto_num_int)
maximo = max(conjunto_num_int)
print(f'O valor minimo do conjunto é: ', minimo, ' e o valor maximo é: ', maximo)
input()

#6 Crie um conjunto com as cores do arco-íris (vermelho, laranja, amarelo, verde,azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor digitada está no conjunto e imprima uma mensagem correspondente.
print("6-Arco-Iris")
conjunto_arco_iris = {'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta'}
cor = input("Digite uma Cor: ")
if cor in conjunto_arco_iris:
    print(f'a cor', cor, 'está no arco-iris')
else:
    print(f'a cor', cor, 'não esta no arco-iris')
input()

#7. Crie um conjunto com os dias da semana (segunda, terça, quarta, quinta, sexta, sábado, domingo) e remova os dias úteis (segunda a sexta). Imprima oconjunto resultante.
print("7-Semana")
conjunto_dia_semana = {'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'}
conjunto_dia_semana.remove('segunda')
conjunto_dia_semana.remove('terça')
conjunto_dia_semana.remove('quarta')
conjunto_dia_semana.remove('quinta')
conjunto_dia_semana.remove('sexta')
print(conjunto_dia_semana)
input()

# 8. Crie um conjunto com os números de 1 a 20 e outro conjunto com os números pares de 1 a 10. Imprima a diferença entre os dois conjuntos.
print("8-Diferença")
conjunto_maior = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
conjunto_menor = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(conjunto_maior-conjunto_menor)
input()

#9. Crie um conjunto com as notas de um aluno em uma disciplina e verifique se ele foi aprovado (média 7) ou reprovado (média abaixo de 7).
print("9-Notas")
conjunto_notas = {10, 9.5, 7, 8, 9}
media = sum(conjunto_notas) / len(conjunto_notas)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
input()

#10. Crie um conjunto com os números primos de 1 a 20 e verifique se um número digitado pelo usuário está no conjunto.
print("10-Primos")
conjunto_primos = {2, 3, 5, 7, 11, 13, 17, 19}
numero = input("Digite um número: ")
if numero in conjunto_primos:
    print("O seu número está no conjunto!")

# Dicionários
# 1.Crie um dicionário vazio e adicione duas chaves e valores a ele.

meu_dicionario = {}
meu_dicionario['teste'] = 'correto'
meu_dicionario['liberar'] = 'intervalo'
print(meu_dicionario)

# 2. Crie um dicionário com as chaves &quot;nome&quot;, &quot;idade&quot; e &quot;cidade&quot; e preencha com seus dados. Imprima o dicionário.

meu_dicionario = {}
meu_dicionario2 = {'nome':'João','Idade':30,'Cidade':'Guarapuava'}
print(meu_dicionario2)

# 3. Crie um dicionário com o nome e o preço de três produtos diferentes. Imprima o dicionário.

dicionario_nome = {'nome': 'Gustavo','Preço 1' : 'R$29','Preço 2': 'R$25','Preço 3': 'R$45' }
print(dicionario_nome)

# 4. Crie um dicionário com o nome de três estados e suas respectivas capitais. Peça ao usuário para digitar um estado e imprima a capital correspondente.

dicionario4 = {'Paraná': 'Curitiba', 'Minas Gerais': 'Belo Horizonte', 'Santa Catarina': 'Florianópolis'}

dicionarioL = input('\nA = Paraná \nB = Minas Gerais \nC = SantaCatarina \nEscolha um estado: ')
if dicionarioL == 'A' and dicionarioL == 'a' :
    print(dicionario4['Paraná'])
elif dicionarioL == 'B' and dicionarioL == 'b' :
    print(dicionario4['Minas Gerais'])
else:
    print(dicionario4['Santa Catarina'])

# 5. Crie um dicionário com o nome de cinco cidades e suas respectivas populações. Imprima a cidade com a maior população.
dicionario5 = {'Guarapuava': 182.644, 'Curitiba': 1773.733, 'Pindamonhangaba': 170.132, 'Caraguatatuba': 132.558, 'Londrina': 575.377}
valores = dicionario5.values()
print("Maior população:",max(valores))

# 6. Crie um dicionário com o nome de três alimentos e suas respectivas calorias. Peça ao usuário para digitar um alimento e imprima a quantidade de calorias correspondente.

dicionario6 = {'100g de Arroz': 130, '100g de Feijão': 350, '100g de Carne Vermelha': 288}

dicionarioC = input('\n1 = 100g de Arroz \n2 = 100g de Feijão \n3 = 100g de Carne Vermelha \nEscolha um alimento: ')
if dicionarioC == '1' :
    print("Calorias do Arroz:",dicionario6['100g de Arroz'],"kcal")
elif dicionarioC == '2' :
    print("Calorias do Feijão:",dicionario6['100g de Feijão'],"kcal")
elif dicionarioC == '3' :
    print("Calorias da Carne Vermelha:",dicionario6['100g de Carne Vermelha'],"kcal")

# 7. Crie um dicionário com o nome de cinco animais e suas respectivas clasificações (mamífero, ave, réptil, etc.). Imprima apenas os nomes dos animais.
animais = {"Cachorro": "mamífero","Papagaio": "ave","Cobra": "réptil","Gato": "mamífero","Tartaruga": "réptil"}
for animal in animais:
    print(animal)

# 8. Crie um dicionário com o nome de cinco países e suas respectivas bandeiras. Imprima apenas os nomes dos países.
paises = {"Brasil": "bandeira_brasil.png","Estados Unidos": "bandeira_eua.png","França": "bandeira_franca.png","Japão": "bandeira_japao.png","Austrália": "bandeira_australia.png"}
for pais in paises:
    print(pais)

# 9. Crie um dicionário com o nome de cinco frutas e suas respectivas cores. Imprima o nome de cada fruta seguido de sua cor.
frutas = {"Maçã": "Vermelho","Banana": "Amarelo","Uva": "Roxo","Laranja": "Laranja","Morango": "Vermelho"}
for fruta, cor in frutas.items():
    print(fruta + ": " + cor)

# 10. Crie um dicionário com o nome de três jogos e a quantidade de jogadores necessária. Peça ao usuário para digitar um jogo e imprima a quantidade de jogadores correspondente.
jogos = {"COD": 12,"R6": 10,"CS": 10}

jogo_digitado = input("Digite o nome de um jogo: ")

if jogo_digitado in jogos:
    quantidade_jogadores = jogos[jogo_digitado]
    print(f"O jogo {jogo_digitado} requer {quantidade_jogadores} jogadores.")
else:
    print("Jogo não encontrado no dicionário.")
    
#Tuplas
#1. Crie uma tupla com os números de 1 a 5 e imprima a tupla.
minha_tupla = (1,2,3,4,5)
print (minha_tupla)

#2. Crie uma tupla com os nomes de três países e imprima o segundo elemento da tupla.
tupla_paises = ('França','Inglaterra','Brasil')
print (tupla_paises[1])

#3. Crie uma tupla com os valores de uma conta de restaurante (valor da refeição, taxa de serviço e valor total). Imprima a tupla.
tupla_restaurante = {'valor da refeição': 79.90 , 'taxa': 7.90 , 'valor total': 87.80}
print (tupla_restaurante)

#4. Crie uma tupla com os nomes de cinco pessoas e peça ao usuário para digitar um número entre 1 e 5. Imprima o nome correspondente ao número digitado.
tupla_nomes = ("Guga", "Rafa", "Fer", "Julia", "João")
tupla_numero = int(input("Digite um número entre 1 e 5: "))
if tupla_numero >= 1 and tupla_numero <= 5:
    tupla_escolha = tupla_nomes[tupla_numero - 1]
    print("O nome escolhido é:", tupla_escolha)
else:
    print("Número inválido. Digite um número entre 1 e 5.")
    
#5. Crie uma tupla com as notas de um aluno em uma disciplina e imprima a média das notas.
tupla_notas = (8.5, 7.0, 9.2, 6.8, 9.5)
tupla_media = sum(tupla_notas) / len(tupla_notas)
print("A média das notas é:", tupla_media)

#6. Crie uma tupla com as cores do arco-íris (vermelho, laranja, amarelo, verde, azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor digitada está na tupla e imprima uma mensagem correspondente.
tupla_cores_arco_iris = ('vermelho','Vermelho', 'laranja','Laranja', 'amarelo','Amarelo', 'verde','Verde', 'azul','Azul', 'anil','Anil', 'violeta','Violeta')
tupla_cor_digitada = input("Digite uma cor: ")
if tupla_cor_digitada in tupla_cores_arco_iris:
    print(f"A cor {tupla_cor_digitada} está presente no arco-íris!")
else:
    print(f"A cor {tupla_cor_digitada} não faz parte do arco-íris.")

#7. Crie uma tupla com as temperaturas de uma semana (sete dias) e imprima a temperatura máxima e mínima da semana.
tupla_temperaturas = (28, 30, 25, 27, 29, 31, 26)
tupla_temperatura_maxima = max(tupla_temperaturas)
tupla_temperatura_minima = min(tupla_temperaturas)
print(f"Temperatura máxima da semana: {tupla_temperatura_maxima}°C")
print(f"Temperatura mínima da semana: {tupla_temperatura_minima}°C")

#8. Crie uma tupla com os nomes de cinco frutas e suas respectivas cores. Imprima o nome de cada fruta seguido de sua cor.
tupla_frutas_cores = (("Maçã", "Vermelha"),("Banana", "Amarela"),("Laranja", "Laranja"),("Uva", "Roxa"),("Pera", "Verde"))
for tupla_fruta, tupla_cor in tupla_frutas_cores:
    print(f"{tupla_fruta}: {tupla_cor}")

#9. Crie uma tupla com os números de 1 a 10 e outra tupla com os números de 5 a 15. Imprima a interseção entre as duas tuplas.
tupla1_numeros = tuple(range(1, 11))
tupla2_numeros = tuple(range(5, 16))
tupla_intersecao = set(tupla1_numeros) & set(tupla2_numeros)
print("Interseção entre as tuplas:")
for tupla_numero in tupla_intersecao:
    print(tupla_numero)

#10. Crie uma tupla com as letras do alfabeto e uma segunda tupla com as vogais. Imprima a diferença entre as duas tuplas.
tupla_alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
tupla_vogais = ('a', 'e', 'i', 'o', 'u')
tupla_diferenca = tuple(letra for letra in tupla_alfabeto if letra not in tupla_vogais)
print("Diferença entre as duas tuplas:", tupla_diferenca)