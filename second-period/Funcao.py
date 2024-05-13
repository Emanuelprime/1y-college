def primeiraFuncao(): #Assinatura da função
  print("Minha primeira função! ")

primeiraFuncao()

#parametros (Aparecem dentro dos parenteses)
def imprimeNome(nome):
  print(f'Nome: {nome}')

imprimeNome('Joao')
imprimeNome('Thomas')

def montaComputador(cpu, armazenamento, memoria):
  print(f'A configuração é:\n \n\t - CPU: {cpu} \n\t - Armazenamento: {armazenamento}TB \n\t - Memória: {memoria}GB RAM')

montaComputador('Ryzen 5', 1, 32)

#PROCEDIMENTO: Função sem retorno
#FUNÇÃO: Retorno

def somaValores(valor1, valor2):
  soma = valor1 + valor2
  return soma


resultado = somaValores(10, 30)
print(f'O valor da soma é: {resultado}')
print(f'O valor da soma é:', somaValores(34,45))


def entradaValores(valor):
  soma = 0
  while(valor > 0):
    soma += valor
    valor -= 1
  print(f'A soma é: ', soma)
resultado = entradaValores(15)
