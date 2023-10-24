# Carros.py
class Carros:
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

# Veiculos.py


class Veiculos:
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

    def descricao(self):
        print(f"Tipo de veículo: {self._tipo}")
        print(f"Velocidade: {self._velocidade} km/h")


class Carro(Veiculos):
    def __init__(self, tipo, velocidade, marca):
        super().__init__(tipo, velocidade)
        self._marca = marca

    def descricao(self):
        super().descricao()
        print(f"Marca: {self._marca}")
        print("Este veículo é um carro.")


class Moto(Veiculos):
    def __init__(self, tipo, velocidade, cilindrada):
        super().__init__(tipo, velocidade)
        self._cilindrada = cilindrada

    def descricao(self):
        super().descricao()
        print(f"Cilindrada: {self._cilindrada} cc")
        print("Este veículo é uma moto.")
