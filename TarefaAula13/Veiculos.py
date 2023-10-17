class Veiculos:
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade
    def descricao(self, descricao_veiculo):
        print(f'A descrição do veiculo é: {descricao_veiculo}')

class Carro(Veiculos):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)
class Moto(Veiculos):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)


