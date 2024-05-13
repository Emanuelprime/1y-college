print("Quantos pãezinhos foram vendidos?")
p = float(input())
print("Quantas broas foram vendidos?")
b = float(input())
valorp = p * 0.80
valorb = b * 2.50
total = valorb + valorp
fabric = total * 0.43
poupanca = (total - fabric) * 0.15
euro = poupanca / 4.6
print("O Total vendido foi:",total)
print("O valor de fabricação dos pães e broas é:", fabric)
print("O Valor guardado na poupança foi de:", round(poupanca, 2))
print("A Quantidade de euro que ele guardou foi:", round(euro, 2))

