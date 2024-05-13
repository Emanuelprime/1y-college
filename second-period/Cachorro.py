from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca, cor):
        super().__init__(nome,especie="Cachorro")
        self._raca = raca
        self._cor = cor

    def emitirSom(self):
        print(f"{self._nome} late. (au au)")

    def dormindo(self):
        print(f"{self._nome} está dormindo")

    def buscar(self):
        print(f"{self._nome} busca a bola")

    def comendo(self):
        print(f"{self._nome} está se alimentando")
