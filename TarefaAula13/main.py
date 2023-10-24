
from Veiculos import Carro, Moto, Veiculos, Carros, acelerar

# Exemplo de uso
# Exercicio 1
c1 = Carros('Fusca', 1938)
print("Exercício 1:", c1.get_modelo(), c1.get_ano())

# Exercicio 2
c1.set_ano(2000)
c1.set_modelo("Golf")
print("Exercício 2:", c1.get_modelo(), c1.get_ano())

# Exercicio 3
c2 = Carro("Conversível", 240, "AUDI")
m1 = Moto("Esportiva", 200, "1200")
print("Exercício 3 Carro:", c2._tipo, c2._velocidade)
print("Exercício 3 Moto:", m1._tipo, m1._velocidade)

# Exercicio 4
c2.descricao()
m1.descricao()

# Exercicio 5
print("Velocidade inicial do carro:", c2._velocidade, "km/h")
print("Velocidade inicial da moto:", m1._velocidade, "km/h")

acelerar(c2)
acelerar(m1)

print("Velocidade após acelerar o carro:", c2._velocidade, "km/h")
print("Velocidade após acelerar a moto:", m1._velocidade, "km/h")
