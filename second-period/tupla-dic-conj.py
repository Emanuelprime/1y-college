'''Conjuntos

#Criando um conjunto vazio:
conjunto_vaz = set()
conjunto2 = {1,2,3,4,}

conjunto2.add(8)
conjunto2.remove(2)

#Verificar se o elemento está no conjunto
if 3 in conjunto2:
   # print("O conjunto contém o elemento 3")

#Operações da Loli
#União
conjunto1 = {1,2,3}
conjunto3 = {2,10,11}
uniao = conjunto1.union(conjunto3)

#print(uniao)
#Intersecção
intersecao = conjunto1.intersection(conjunto3)
#print(intersecao)

#Diferença
diferenca = conjunto1.difference(conjunto3)
print(diferenca)'''

#Dicionarios
meu_dicionario = {}
meu_dicionario2 = {'nome': 'Lucas','idade':24,'cidade':'Guarapuava'}

#Adicionar elementos
meu_dicionario2['profissao'] = 'programador'

#Remover elementos
del meu_dicionario2['cidade']
#print(meu_dicionario2)

#Verificar a existencia de uma chave
if 'idade'in meu_dicionario2:
   '''print("A chave 'idade' existe no dicionario")'''

chaves = meu_dicionario2.keys()
valores =meu_dicionario2.values()

#percorrer um dicionario
for chaves,valor in meu_dicionario2.items():
  '''  print(chaves,valor)

#mesclar dois dicionarios
meu_dicionario3 = {'sobrenome':'Silvs', 'Telefone':'988037573',}
meu_dicionario2.update(meu_dicionario3)
print(meu_dicionario2)
'''

  #Tuplas
  minha_tupla = ()
  minha_tupla2 = (1,2,3,'quatro','cinco',6.0)

#Mesclar tuplas
minha_tupla3 = ('a','b','c')
nova_tupla = minha_tupla2 + minha_tupla3
print(nova_tupla)

#Verificar a existência de um valor na tupla
if 'quatro' in minha_tupla2:
    print("O elemento 'quatro' existe na tupla")

#percorrer a tupla
for elemento in minha_tupla2:
    print(elemento)
