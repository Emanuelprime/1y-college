#1 Crie uma classe chamada Carro com atributos encapsulados (_modelo e _ano) e métodos para obter e definir esses atributos.
from Carros import Carros

c1 = Carros('Fusca',1938)
print("Exercicio 1", c1._Carros__modelo, c1._Carros__ano)

#2 Modifique a classe Carro do exercício anterior para usar atributos privados (__modelo e __ano) e métodos de acesso para obter e definir esses atributos.
c1.ano = 2000
c1.modelo = "Golf"
print("Exercicio 2", c1.modelo, c1.ano)

#3 Crie uma classe Veiculo com atributos como tipo e velocidade e, em seguida, crie classes Carro e Moto que herdem de Veiculo.
from Veiculos import Carro, Moto
c2 = Carro("Conversível", 240, "TEste")
m1 = Moto("Esportiva", 200, "teste")
print("Exercicio 3 Carro:", c2._tipo, c2._velocidade)
print("Exercicio 3 Moto:", m1._tipo, m1._velocidade)

#4 Na classe Veiculo, crie um método chamado descricao() que imprima uma descrição básica do veículo. Sobrescreva esse método nas classes Carro e Moto para fornecer descrições específicas para cada tipo de veículo.

c2.descricao = "teste"
