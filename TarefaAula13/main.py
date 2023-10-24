
from Veiculos import Carro, Moto, Veiculos, Carros

# Exemplo de uso
# Exercício 1
c1 = Carros('Fusca', 1938)
print("Exercício 1:", c1.get_modelo(), c1.get_ano())

# Exercício 2
c1.set_ano(2000)
c1.set_modelo("Golf")
print("Exercício 2:", c1.get_modelo(), c1.get_ano())

# Exercício 3
c2 = Carro("Conversível", 240, "TEste")
m1 = Moto("Esportiva", 200, "teste")
print("Exercício 3 Carro:", c2._tipo, c2._velocidade)
print("Exercício 3 Moto:", m1._tipo, m1._velocidade)

# Exercício 4
c2.descricao()
