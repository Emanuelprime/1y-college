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
def decimal_Binario (numero4):
    if numero4 == 0:
        return "0"
    pilha = []
    while numero4 > 0:
        sobra = numero4 % 2

        pilha.append(str(sobra))
        numero4//= 2
    binario = ""
    while pilha:
        binario+=pilha.pop()
    return binario
NUmero_Binario = int(input('Digite um numero: '))
Bi_DEC = decimal_Binario(NUmero_Binario)
print(Bi_DEC)
'''5 Implemente um histórico de comandos de um editor de texto simples usando uma
pilha. A cada vez que um comando é executado, ele é adicionado à pilha.
Implemente a capacidade de desfazer um comando usando a pilha.'''
def criar_editor_de_texto():
    texto = ""
    pilha_comandos = []

    def executar_comando(comando):
        nonlocal texto, pilha_comandos
        texto += comando
        pilha_comandos.append(comando)

    def desfazer_comando():
        nonlocal texto, pilha_comandos
        if pilha_comandos:
            ultimo_comando = pilha_comandos.pop()
            texto = texto[:-len(ultimo_comando)]

    def imprimir_texto():
        nonlocal texto
        print(texto)

    def historico():
        nonlocal pilha_comandos
        [desfazer_comando() for _ in pilha_comandos]

    return {
        "executar_comando": executar_comando,
        "desfazer_comando": desfazer_comando,
        "imprimir_texto": imprimir_texto,
        "historico": historico
    }
editor = criar_editor_de_texto()
editor["executar_comando"]("Digite isso. ")
editor["executar_comando"]("Agora isso. ")
editor["executar_comando"]("E mais isso. ")
editor["imprimir_texto"]() 
print("Desfazendo comandos:")
editor["historico"]()
editor["imprimir_texto"]()  