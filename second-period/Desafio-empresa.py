contador = 0
for i in range(10):
    nomes = input("Digite o nome do cliente:")
    compra = float(input("Digite o valor da compra:"))
    if compra >= 1500:
        desconto = compra * 0.20
    else:
        desconto = compra * 0.15
        nvvalor = compra - desconto
    print(f'O cliente {nomes} gastou {compra} e obteve o desconto de {desconto}, gastando apenas {nvvalor}')
    contador = contador + desconto
    print(f'O desconto total foi de {contador}')
