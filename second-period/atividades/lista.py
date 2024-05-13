nomes = ["joao", "jose", "Paulo", "Lucas", "Gabriel"]
idades = [17, 18, 22, 27, 33]
del nomes[2], idades[2]
for i in range(len(idades)):
    if idades[i] >= 18:
        print(nomes[i], "é maior de idade")
    else:
        print(nomes[i], "é menor de idade")

nomes.append("Arthur")
idades.append(15)
print("======================================")
for i in range(len(idades)):
    if idades[i] >= 18:
        print(nomes[i], "é maior de idade")
    else:
        print(nomes[i], "é menor de idade")
